#!/usr/bin/env python3

"""
Tento skript umožní rozřadit soubory podle přípon do složek podle toho,
zda je soubor obrázek, video, dokument, musescore nebo zip.
"""
import os
import shutil
import json
import argparse
import enum

class Color(str, enum.Enum):
    """
    Console colors.
    """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# helper functions -
def retry_on_err(err, msg = None):
    """
    Decorator for retrying function on specific error.
    Message to be printed on error can be provided.
    """
    def wrapper(func):
        def wrapped(*args, **kwargs):
            fn_succ = False
            while not fn_succ:
                try:
                    func(*args, **kwargs)
                    fn_succ = True
                except err:
                    if msg:
                        print(msg)
                    continue
        return wrapped
    return wrapper

@retry_on_err(OSError,
f"{Color.RED}Složka neexistuje. Zadejte prosím existující složku.{Color.END}")
def prompt_chdir():
    """
    Prompts user for new working directory.
    """
    print(f"{Color.PURPLE}Zadejte absolutní cestu do složky k roztřízení {Color.END}.")
    print("Zanechte prázdné pro aktuální složku.")
    adresa = input()
    if adresa != "":
        os.chdir(adresa)

def read_config(cfg_file = "config.json") -> dict:
    """
    Reads config file and returns a extension and path dictionary.
    """
    with open(cfg_file, 'r', encoding='utf-8') as file:
        cfg = json.load(file)
    extensions = {}
    paths = {}
    for key, item in cfg.items():
        for ext in item["extensions"]:
            extensions[ext] = key
        paths[key] = item["path"]
    return (extensions, paths)

def organize_files(root_path: str, suffices: dict,
    paths: dict, dry_run: bool = False):
    """
    Moves file according to suffix and path dictionary.
    """
    dry_run_paths = set()
    for file in os.listdir():
        try:
            file_suffix = os.path.splitext(file)[1]
            if not file_suffix:
                continue

            file_type = suffices.get(file_suffix[1:].lower(), None)
            if file_type is None:
                continue

            path = os.path.join(root_path, paths[file_type])
            if (not os.path.exists(path)) and (not os.path.isdir(path)):
                if not dry_run:
                    os.makedirs(path)
                if dry_run and (paths[file_type] not in dry_run_paths):
                    dry_run_paths.add(paths[file_type])
                    print(f"{Color.RED}DRY RUN - Vytvoření složky: {path}{Color.END}")

            if not dry_run:
                shutil.move(file, path)
            print(f"Soubor {file} je typu {file_type} a je přesunut do složky {paths[file_type]}")
        except OSError as err:
            print(f"{Color.RED}Soubor {file} z nějakého důvodu nelze přesunout:{Color.END}")
            print(err)

# MAIN PROGRAM

def main(args):
    """
    Main program.
    """
    # read config
    (suffices, paths) = read_config(args.config)
    # intro
    print(f"{Color.GREEN}{Color.BOLD}ORGANIZE{Color.END}")
    print("Autor: Miroslav Burýšek")
    print(
    "Tento program třídí soubory na hudbu, obrázky, filmy, dokumenty, zip, musescore a ostatní.")

    if args.dry_run:
        print(f"{Color.RED}DRY RUN - Změny nebudou provedeny{Color.END}")

    # přechod do složky
    prompt_chdir()
    print(f"Nacházím se ve složce: {Color.PURPLE}{Color.BOLD}{os.getcwd()}{Color.END}")

    if not args.dry_run:
        approval = ("y", "yes")
        approval_input = input("Přejete si roztřídit soubory? [Y/n] ").lower()

        if approval_input not in approval: # task declined
            print("Dobře. Hezký den i Vám.")
            return

    # třídění
    organize_files(args.root or os.getcwd(), suffices, paths, args.dry_run)
    if not args.dry_run:
        print(f"{Color.BOLD}{Color.GREEN}Soubory úspěšně přesunuty. Přeji hezký den.{Color.END}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Tento skript umožní rozřadit soubory podle přípon do složek podle nastavení."
    )
    parser.add_argument('--dry-run', default=False, required=False, action='store_true')
    parser.add_argument('--config', type=str, default="config.json", required=False)
    parser.add_argument('--root', type=str, default=None, required=False)
    pargs = parser.parse_args()
    main(pargs)
