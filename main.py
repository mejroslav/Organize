#!/usr/bin/env python3
"""
Tento skript umožní rozřadit soubory podle přípon do složek podle toho, zda je soubor obrázek, video, dokument, musescore nebo zip. 
"""

import organizeFunctions
import settings

# MAIN PROGRAM


def main():
    # intro
    organizeFunctions.print_intro()
    organizeFunctions.check_for_valid_paths()
    directory = organizeFunctions.set_directory()

    # sorting
    decline_task = {"n", "nn", "ne", "no", "nikdy", "stop"}
    approve_task = {"y", "yy", "ano", "yes", "jo", "ok", "pls"}
    while True:
        user_approval = input("""Přejete si roztřídit soubory? [y/n] """).lower()

        if user_approval in approve_task:
            organizeFunctions.organize_files(directory)
            print(
                settings.color.BOLD
                + settings.color.GREEN
                + "Soubory úspěšně přesunuty."
                + settings.color.END
            )
            break
        elif user_approval in decline_task:
            break
        else:
            print("Zadejte prosím jeden z požadovaných výrazů [y/n].")
    organizeFunctions.escape()


if __name__ == "__main__":
    main()
