#!/usr/bin/env python3

"""
Tento skript umožní rozřadit soubory podle přípon do složek podle toho, zda je soubor obrázek, video, dokument, musescore nebo zip. 
"""
import os
import shutil
import sys


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
    "directory": (""),
    "audio": (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv"),
    "video": (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf", ".avi", ".mkv"),
    "img": (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif"),
    "document": (".pdf", ".djvu", ".doc", ".docx", ".odt", ".html", ".css", ".pptx", ".md", ".chm"),
    "musescore": (".mscz"),
    "zipfile": (".zip")
}

# U každého uživatele potřeba změnit!
root_path = os.path.expanduser("~") 
paths = {
    "directory": "Documents",
    "audio": "Music",
    "video": "Videos",
    "img": "Pictures",
    "document": "Documents",
    "musescore": "Documents/MuseScore3Development/Notové zápisy", # používání musescore souborů
    "zipfile": "Documents",
}


def get_type_from_sfx(file_suffix: str) -> str:
    """Given suffix of the file, return the type of file according to the `suffices` dictionary.

    Args:
        file_suffix (str): A suffix after the "dot" symbol in filename, i.e.: ".avi", ".pdf", ".txt"

    Returns:
        str: "directory", "audio", "video", "img", "document", "musescore", "zipfile"
    """
    for type in suffices:
        if file_suffix in suffices[type]:
            return type

def get_path_from_ftype(filetype: str) -> str:
    """Given filetype from `get_type_from_sfx`, return the path for the file according to the `paths` dictionary.

    Args:
        filetype (str): "directory", "audio", "video", "img", "document", "musescore", "zipfile"

    Returns:
        str: A path from the `paths` dictionary.
    """
    return f"{root_path}/{paths[filetype]}/"

def organize_files():
    for file in os.listdir():
        try:
            file_suffix = os.path.splitext(file)[1]
            file_type = get_type_from_sfx(file_suffix)
            path = get_path_from_ftype(file_type)
            shutil.move(file, path)
            print(f"name: {file}, type: {file_type}, destination: {paths[file_type]}")
        except OSError as err:
            print(f"name: {file} {color.RED}nelze přesunout{color.END}")
            print(err)
        except KeyError as err:
            print(f"name:{file}, {color.YELLOW}neznámý typ souboru{color.END}")
            


def set_directory():
    """Change the directory if necessary.
    """
    escape_sequences = {"exit", "stop", "break", "exit()", "konec"}
    
    while True:
        adresa = input("Zadejte absolutní cestu do složky, ze které chcete roztřídit soubory (ENTER pro aktuální adresu, exit pro ukončení): ")
        if adresa == "":
            return None
        elif adresa in escape_sequences:
            escape()
        try:
            os.chdir(adresa)
            return None
        except OSError as err:
            print("Zadaná cesta není platná. Zkuste to znovu.")

def escape():
    print("Hezký den i Vám.")
    exit()

def print_intro():
    """Print the cool header and the program description."""
    print(color.GREEN + """
  ____  _____   _____          _   _ _____ ____________ 
 / __ \|  __ \ / ____|   /\   | \ | |_   _|___  /  ____|
| |  | | |__) | |  __   /  \  |  \| | | |    / /| |__   
| |  | |  _  /| | |_ | / /\ \ | . ` | | |   / / |  __|  
| |__| | | \ \| |__| |/ ____ \| |\  |_| |_ / /__| |____ 
 \____/|_|  \_\\______/_/    \_\_| \_|_____/_____|______|
                                                        
                                                       
Autor: Miroslav Burýšek""" + color.END)
    print("Tento program třídí soubory podle přípon. Zadejte flag -h, --help pro nápovědu.")


# MAIN PROGRAM

def main():
    print_intro()
    set_directory()
    print("""Nacházím se ve složce: """ + color.PURPLE +
          color.BOLD + os.getcwd() + color.END)

    # sorting
    decline_task = ("n", "nn", "ne", "no", "nikdy", "stop")
    approve_task = ("y", "yy", "ano", "yes", "jo", "ok", "pls")
    while True:
        user_approval = input("""Přejete si roztřídit soubory? [y/n] """).lower()
        if user_approval in approve_task:
            organize_files()
            print(color.BOLD + color.GREEN + "Soubory úspěšně přesunuty." + color.END)
            break
        elif user_approval in decline_task:
            break
        else:
            print("Zadejte prosím jeden z požadovaných výrazů [y/n].")
    escape()

if __name__ == '__main__':
    try:
        if sys.argv[1] in {"-h", "--help"}:
            print("Program Organize třídí soubory podle přípon do jednotlivých složek.")
            print(f"""Seznam cest:
            Složky: {get_path_from_ftype("directory")}
            Obrázky: {get_path_from_ftype("img")}
            Videa: {get_path_from_ftype("video")}
            Audio: {get_path_from_ftype("audio")}
            Dokumenty: {get_path_from_ftype("document")}
            MuseScore: {get_path_from_ftype("musescore")}
            ZipFiles: {get_path_from_ftype("zipfile")}
            """)
            escape()
    except IndexError as err:
        pass
    main()
