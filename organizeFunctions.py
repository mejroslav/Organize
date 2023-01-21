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

    for type in settings.extensions:
        if file_extension not in settings.extensions[type]:
            logging.error(f"Unknown file extension: {file_extension}")
            # TODO: vyřešit, co dělat s neznámou příponou
        logging.debug(f"Extension: {file_extension}, return: {type}.")
        return type


def path_for_file(filetype: str) -> str:
    """Given type of file, return its path. It can be modified in `paths.json`.

    Usage:
    >>> path_for_file("document")
    "/home/user/Documents"
    """
    try:
        path = os.path.join(
            settings.ROOT_PATH, settings.paths[filetype]
        )  # /home/mir/Documents
        if os.path.isdir(path):
            logging.debug(f"The path for {filetype}: {path} is a valid path.")
            return path
        else:
            logging.error(f"{filetype}: {path} does not exist.")
    except OSError as err:
        logging.error(err)


def check_for_valid_paths() -> bool:
    for dir in settings.paths.values():
        path = os.path.join(settings.ROOT_PATH, dir)
        if os.path.isdir(path):
            logging.debug(f"{path} is valid")
        else:
            logging.error(f"{path} is not valid")

def organize_files(path) -> None:
    directory = os.path.abspath(path)
    for file in os.listdir(directory):
        try:
            _, ext = os.path.splitext(file)
            file_type = document_type(ext)
            start_point = os.path.join(directory,file)
            end_point = path_for_file(file_type)
            shutil.move(start_point, end_point)
            logging.info(
                f"name: {file}, type: {file_type}, destination: {end_point}"
            )
        except Exception as err:
            logging.error(err)


def set_directory() -> str:
    """The user enter the directory in which all files should be organized."""
    while True:
        working_directory = os.getcwd()
        user_path_input = input(
            "Zadejte absolutní cestu do složky, ze které chcete roztřídit soubory (ENTER pro aktuální adresu, exit pro ukončení): "
        )
        path = os.path.join(working_directory, user_path_input)
        if os.path.isdir(path):
            logging.info(f"Address {path} is valid.")
            return path
        else:
            logging.error(f"Address {path} is not valid!")


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
                                                        
                                                       
Autor: Miroslav Burýšek"""
        + settings.color.END
    )
    print(
        "Tento program třídí soubory podle přípon. Zadejte flag -h, --help pro nápovědu."
    )


def escape():
    print("Hezký den i Vám.")
    exit()
