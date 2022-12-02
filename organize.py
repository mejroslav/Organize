#!/usr/bin/env python3

"""
Tento skript umožní rozřadit soubory podle přípon do složek podle toho, zda je soubor obrázek, video, dokument, musescore nebo zip. 
"""
import os
import shutil
import time


class color:
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


suffices = {
    "audio": (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv"),
    "video": (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf"),
    "img": (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif"),
    "document": (".pdf", ".djvu", ".doc", ".docx"),
    "musescore": (".mscz"),
    "zipfile": (".zip")
}

# U každého uživatele potřeba změnit!
root_path = "/home/mir" 
paths = {
    "audio": "Music",
    "video": "Videos",
    "img": "Pictures",
    "document": "Documents",
    "musescore": "Documents/MuseScore3Development/Notové zápisy",
    "zipfile": "Documents",
}


def get_type_of_file(file_suffix: str) -> str:
    '''
    Vrací typ souboru ze slovníku suffices.
    '''
    for type in suffices:
        if file_suffix in suffices[type]:
            return type

def path_for_file(filetype: str) -> str:
    '''
    Vrací cestu, kam bude soubor přesunut.
    '''
    return f"{root_path}/{paths[filetype]}/"

def organize_files():
    for file in os.listdir():
        try:
            file_suffix = os.path.splitext(file)[1]
            file_type = get_type_of_file(file_suffix)
            path = path_for_file(file_type)
            shutil.move(file, path)
            print(f"Soubor {file} je typu {file_type} a je přesunut do složky {paths[file_type]}")
        except OSError as err:
            print(f"{color.RED}Soubor {file} z nějakého důvodu nelze přesunout:{color.END}")
            print(err)


def set_directory():
    adresa = input("""Zadejte absolutní cestu do složky, ze které chcete roztřídit soubory (ENTER pro aktuální adresu): """)
    if adresa != "":
        try:
            os.chdir(adresa)
        except OSError as err:
            print("Zadaná cesta není platná. Zkuste to znovu.")
            set_directory()



# MAIN PROGRAM

def main():
    # intro
    print(f"{color.GREEN}{color.BOLD}ORGANIZE{color.END}")
    print("Autor: Miroslav Burýšek")
    print("Tento program třídí soubory na hudbu, obrázky, filmy, dokumenty, zip, musescore a ostatní.")

    # přechod do složky
    set_directory()
    print("""Nacházím se ve složce: """ + color.PURPLE +
          color.BOLD + os.getcwd() + color.END)

    # třídění
    decline_task = ("n", "nn", "ne", "no", "stop", "end", "konec")
    user_approval = input("""Přejete si roztřídit soubory? [Y/n] """).lower()

    if user_approval in decline_task: # task declined
        print("Dobře. Hezký den i Vám.")
        exit()
    else:
        organize_files()
        print(color.BOLD + color.GREEN + "Soubory úspěšně přesunuty. Přeji hezký den.")


if __name__ == '__main__':
    main()
