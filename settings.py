"""Configuration settings. Logging, colors, extensions and paths."""

import logging
import json
import os
import optparse

# Logging configuration
logging.basicConfig(level=logging.DEBUG)

# U každého uživatele potřeba změnit!
ROOT_PATH = os.path.expanduser("~")

with open("extensions.json", "r", encoding="utf-8") as file:
    extensions = json.loads(file.read())
with open("paths.json", "r", encoding="utf-8") as file:
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


