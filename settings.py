"""Configuration settings. Logging, colors, extensions and paths."""

import logging
import json
import os
import optparse

# U každého uživatele potřeba změnit!
ROOT_PATH = os.path.expanduser("~")
PARENT_FOLDER = os.path.dirname(__file__)

EXTENSIONS_FILE = os.path.join(PARENT_FOLDER, "extensions.json")
PATHS_FILE = os.path.join(PARENT_FOLDER, "paths.json")

with open(EXTENSIONS_FILE, "r", encoding="utf-8") as file:
    extensions = json.loads(file.read())
with open(PATHS_FILE, "r", encoding="utf-8") as file:
    paths = json.loads(file.read())


class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def parse_arguments():
    parser = optparse.OptionParser()

    parser.add_option(
        "-v",
        "--verbose",
        help="Log addition info.",
        dest="verbose",
        action="store_true",
        default=False,
    )
    
    options, args = parser.parse_args()
    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
