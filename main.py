#!/usr/bin/env python3
"""
Tento skript umožní rozřadit soubory podle přípon.

V souboru `extensions.json` jsou uloženy přípony pro jednotlivé typy souborů.
V souboru `paths.json` jsou uloženy cílové destinace pro jednotlivé typy souborů.
"""

import logging
import organizeFunctions
import settings


def main() -> None:
    "The main function. Organize files in given directory."
    organizeFunctions.print_intro()
    valid_paths = organizeFunctions.check_for_valid_paths()
    if not valid_paths:
        raise Exception("Některé cílové destinace nejsou platné adresy. Můžete je změnit v souboru 'paths.json'.")
    directory = organizeFunctions.set_directory()
    approval = organizeFunctions.wait_for_user_approval()
    if approval:
        organizeFunctions.organize_files(directory)
    organizeFunctions.escape()


if __name__ == "__main__":
    settings.parse_arguments()
    main()