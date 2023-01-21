"""Functions for organizing files."""

import os
import shutil
import logging

import settings


def document_type(file_extension: str) -> str:
    """Given extension of the file, return the type of file. It can be modified in `extensions.json`.

    Args:
        file_extension (str): An extension is everything after the "dot" symbol in filename, i.e.: ".avi", ".pdf", ".txt"

    Returns:
        str: A type of given file.

    ---
    Usage:
    >>> document_type(".avi")
    "video"
    >>> document_type(".pdf")
    "document"
    """

    list_of_filetypes = settings.extensions.keys()
    for filetype in list_of_filetypes:
        if file_extension in settings.extensions[filetype]:
            logging.debug(f"Extension: {file_extension}, return: {filetype}.")
            return filetype

    logging.error(f"Unknown file extension: {file_extension}")
    # TODO: vyřešit, co dělat s neznámou příponou


def path_for_file(filetype: str) -> str:
    """Given type of file, return its path. It can be modified in `paths.json`.

    ---

    Usage:
    >>> path_for_file("document")
    "/home/user/Documents"
    >>> path_for_file("audio")
    "/home/user/Music"
    """
    try:
        path = os.path.join(
            settings.ROOT_PATH, settings.paths[filetype]
        )
        if os.path.isdir(path):
            logging.debug(f"The path for {filetype}: {path} is a valid path.")
            return path
        else:
            logging.error(f"{filetype}: {path} does not exist.")
    except OSError as err:
        logging.error(err)
    except KeyError as err:
        pass

def move_file(root_path: str, filename: str) -> None:
    """Move file to its destination. If it is a folder, do nothing."""
    
    start_point = os.path.join(root_path, filename)
    
    if os.path.isdir(start_point):
        logging.info(f"name: {filename}, type: directory")
    elif os.path.isfile(start_point):
        _, ext = os.path.splitext(filename)
        file_type = document_type(ext)
        end_point = path_for_file(file_type)
        
        if end_point:
            try:
                shutil.move(start_point, end_point)
                logging.info(
                    f"name: {filename}, type: {file_type}, destination: {end_point}"
                )
            except Exception as err:
                logging.error(err)
    

def check_for_valid_paths() -> bool:
    """Check if all paths in `paths.json` exist."""
    for dir in settings.paths.values():
        path = os.path.join(settings.ROOT_PATH, dir)
        if os.path.isdir(path):
            logging.debug(f"{path} is a valid path.")
        else:
            logging.error(f"{path} is a not valid path!")
            return False
    logging.debug(f"All paths are valid.")
    return True


def organize_files(path: str) -> None:
    """Move files from folder in path. Do nothing for directories."""
    abs_path = os.path.abspath(path)
    list_of_files = os.listdir(abs_path)

    if list_of_files == []:
        logging.info(f"Directory {abs_path} is empty.")
    else:
        for file in os.listdir(abs_path):
            move_file(abs_path, file)
    logging.info("Organization ended successfully.")


def set_directory() -> str:
    """Wait for user to enter the directory in which all files should be organized."""
    while True:
        working_directory = os.getcwd()
        user_path_input = input(
            "Zadejte cestu do složky, ze které chcete roztřídit soubory (ENTER pro aktuální adresu): "
        )
        path = os.path.join(working_directory, user_path_input)
        if os.path.isdir(path):
            logging.info(f"Address {path} is valid.")
            return path
        else:
            logging.error(f"Address {path} is not valid!")


def wait_for_user_approval() -> bool:
    """Wait for user to approve or disprove organizing."""

    decline_task = {"n", "nn", "ne", "no", "nikdy", "stop"}
    approve_task = {"y", "yy", "ano", "yes", "jo", "ok", "pls"}
    while True:
        user_approval = input("""Přejete si roztřídit soubory? [y/n] """).lower()
        if user_approval in approve_task:
            return True
        elif user_approval in decline_task:
            return False
        else:
            print("Zadejte prosím jeden z požadovaných výrazů [y/n].")


def print_intro():
    """Print the cool header and the program description."""
    print(
        settings.color.GREEN
        + """
  ____  _____   _____          _   _ _____ ____________ 
 / __ \|  __ \ / ____|   /\   | \ | |_   _|___  /  ____|
| |  | | |__) | |  __   /  \  |  \| | | |    / /| |__   
| |  | |  _  /| | |_ | / /\ \ | . ` | | |   / / |  __|  
| |__| | | \ \| |__| |/ ____ \| |\  |_| |_ / /__| |____ 
 \____/|_|  \_\\______/_/    \_\_| \_|_____/_____|______|
                                                        
                                                       
Autor: Miroslav Burýšek

"""
        + settings.color.END
    )
    print(
        """Tento program třídí soubory podle přípon. Zadejte flag -h, --help pro nápovědu.
        """
    )


def escape():
    print("Hezký den i Vám.")
    exit()
