"""Reading text files and saving/loading the game state."""

import os  # os helps us work with folders and file paths

# Work out the folder locations from where this file is,
# so the game works wherever the project folder is placed.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAVE_DIR = os.path.join(BASE_DIR, "saves")  # save files go here
DATA_DIR = os.path.join(BASE_DIR, "data")   # intro.txt and instructions.txt


def read_text_file(filename):
    """Read a text file from the data folder (intro.txt, instructions.txt)."""
    path = os.path.join(DATA_DIR, filename)
    try:
        # "with" closes the file automatically when we are done
        with open(path, "r", encoding="utf-8") as file:  # "r" = read
            return file.read()
    except FileNotFoundError:
        # If the file is missing, show a message instead of crashing
        return f"[{filename} is missing]"


def save_path(name):
    """Return the save file path for a player name."""
    # Keep only letters and numbers so the file name is safe: "Sam!" -> "sam"
    safe = "".join(ch for ch in name.lower() if ch.isalnum()) or "player"
    return os.path.join(SAVE_DIR, safe + ".txt")


def save_exists(name):
    """Return True if this player has a save file."""
    return os.path.exists(save_path(name))


def save_game(name, data):
    """Write the data dictionary to a text file as key=value lines."""
    os.makedirs(SAVE_DIR, exist_ok=True)  # create the saves folder if needed
    with open(save_path(name), "w", encoding="utf-8") as file:  # "w" = write
        for key, value in data.items():
            file.write(f"{key}={value}\n")  # for example: coins=12


def load_game(name):
    """Read a save file and return a dictionary, or None if there is none."""
    if not save_exists(name):
        return None  # None means "nothing"
    data = {}
    with open(save_path(name), "r", encoding="utf-8") as file:
        for line in file:
            if "=" in line:
                # cut the line at the first "=" into a key and a value
                key, value = line.rstrip("\n").split("=", 1)
                data[key] = value
    return data
