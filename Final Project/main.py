"""CALL OF DUTY: Finding Duty - main program (menus and main loop).

This file talks to the player: it asks questions, shows menus and
calls the functions in game/rules.py to do the work.
"""

import os
import sys

# Make sure Python can find the "game" folder, wherever the program is started from
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game import rules, files
from game.rules import Game

TITLE = "CALL OF DUTY: Finding Duty"


def ask_name():
    """Ask for a non-empty player name and return it."""
    while True:  # repeat until we return a valid name
        name = input("What is your name? ").strip()  # strip() removes extra spaces
        if name:
            return name
        print("Please type a name.")


def ask_age():
    """Ask for the age until a whole number is given, and return it."""
    while True:
        text = input("How old are you? ").strip()
        if text.isdigit():   # True only if the text is made of digits
            return int(text)  # turn the text into a number
        print("Please type your age as a number.")


def show_status(game):
    """Print the player's current state."""
    p = game.player
    print(f"\nPlayer: {p.name} (age {p.age})")
    print(f"Location: {p.location.name} | Coins: {p.coins}")
    print("Clinic:", "unlocked" if not game.rooms["Clinic"].locked else "locked")


def show_inventory(game):
    """Print the items the player carries."""
    items = game.player.items
    print("\nInventory:")
    print("\n".join(f"- {item}" for item in items) if items else "(empty)")


def show_clues(game):
    """Print the clues the player has found."""
    clues = game.player.clues
    print("\nClues:")
    print("\n".join(f"- {c}" for c in clues) if clues else "(none yet)")


def choose_location(game):
    """Let the player pick a location by number and travel there."""
    names = list(game.rooms)  # the room names as a list
    for number, name in enumerate(names, start=1):  # numbers start from 1
        print(f"  {number}. {name}")
    choice = input("Go to (number): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(names):
        return rules.travel(game, names[int(choice) - 1])
    return "That is not a place."


def game_loop(game):
    """Main loop of the adventure. Returns when the game ends or player quits."""
    print(f"\nYou are in the {game.player.location.name}.")
    while not game.finished:  # keep playing until Duty is found
        place = game.player.location.name
        # Show the menu (option 4 changes depending on the place)
        print(f"\n--- {place} ---")
        print("1. Search here\n2. Explore a random place\n3. Go to a place")
        print(f"4. {rules.ACTION_LABELS[place]}\n5. Use map")
        print("6. Inventory\n7. Clues\n8. Status\n9. Save game\n0. Back to main menu")
        choice = input("> ").strip().lower()
        # Run the function that matches the player's choice
        if choice == "1":
            print(rules.search_location(game))
        elif choice == "2":
            print(rules.explore_random(game))
        elif choice == "3":
            print(choose_location(game))
        elif choice == "4":
            print(rules.special_action(game))
        elif choice == "5":
            print(rules.use_map(game))
        elif choice == "6":
            show_inventory(game)
        elif choice == "7":
            show_clues(game)
        elif choice == "8":
            show_status(game)
        elif choice == "9":
            game.save()
            print("Game saved!")
        elif choice in ("0", "lopeta"):
            game.save()  # save automatically when leaving
            print("Game saved. Back to the main menu.")
            return
        else:
            print("Unknown command.")
    # The loop ended because Duty was found
    game.save()
    print(f"\n*** CONGRATULATIONS {game.player.name}! You found DUTY and brought him home safely! ***")


def continue_game(name):
    """Load a saved game for this name. Returns a Game or None."""
    data = files.load_game(name)
    if data is None:
        print("No saved game found for that name.")
        return None
    return Game.from_dict(data)


def main():
    """Ask name and age, then show the main menu until 'lopeta'."""
    print(f"=== {TITLE} ===")
    name = ask_name()
    age = ask_age()
    if age < 12:
        # Players under 12 cannot play: show a message and end the program
        print("Sorry, you are a minor. Please play with a grown-up. Goodbye!")
        return
    print(f"\nHello {name}! You are {age} years old.")
    print(files.read_text_file("intro.txt"))  # story text from a file
    while True:  # main menu loop, ends when the player types "lopeta"
        print("\n=== MAIN MENU ===")
        print("1. Start a New Game\n2. Continue a saved game")
        print("3. Instructions\nType 'lopeta' to quit")
        command = input("> ").strip().lower()
        if command == "1":
            game_loop(Game(name, age))
        elif command == "2":
            game = continue_game(name)
            if game is not None:
                if game.finished:
                    print("You already found Duty! Start a new game to play again.")
                else:
                    game_loop(game)
        elif command == "3":
            print(files.read_text_file("instructions.txt"))
        elif command == "lopeta":
            print("Goodbye!")
            break  # leave the loop, the program ends
        else:
            print("Unknown command.")


# Start the game only when this file is run directly (python main.py)
if __name__ == "__main__":
    main()
