"""Game logic for CALL OF DUTY: Finding Duty.

This file decides what happens when the player searches, buys or travels.
It does not ask questions or show menus - main.py does that.
"""

import random  # used for random coins, clues and places

from game.classes import Item, Room, Player
from game import files

# ---------- settings (capital letters = values that never change) ----------
CLINIC_COST = 15   # coins needed to unlock the Clinic
WHISTLE_COST = 5   # price of the dog whistle
BOTTLE_PRICE = 2   # coins paid for each recycled bottle
MAP_BONUS = 10     # coins found by following the map
KEYS_REWARD = 8    # coins for returning the neighbour's keys

# The hint that points the player to the map under the bench
PARK_HINT = "Hint: a child saw something tucked under the old bench in the Park."

# Random clues the player can find when searching
CLUE_POOL = [
    "A neighbour heard a dog barking near the trees at sunset.",
    "Duty's red collar has a bell. Listen for a tiny jingle.",
    "Paw prints lead away from the Neighborhood toward the Forest.",
    "The shopkeeper says Duty loves the sound of a whistle.",
    "A vet nurse says dogs come running when they hear a dog whistle.",
    "Someone saw a golden dog drinking from a stream in the Forest.",
    "A poster on the wall: 'Lost: Golden Retriever named Duty. Please help!'",
]

# Menu text for "special action" (option 4) in each place
ACTION_LABELS = {
    "Park": "Check under the old bench",
    "Shop": "Sell empty bottles for recycling",
    "Neighborhood": "Return lost keys to the neighbour",
    "Clinic": "Buy the dog whistle",
    "Forest": "Look around",
}


def create_rooms():
    """Create all rooms (and the items hidden in them). Returns a dictionary."""
    # A dictionary lets us find a room by name: rooms["Park"]
    return {
        "Park": Room("Park", "A green park with swings, trees and an old bench.",
                     item=Item("Old map", "shows an X behind the Shop")),
        "Shop": Room("Shop", "A small shop that also recycles empty bottles."),
        "Neighborhood": Room("Neighborhood", "Quiet streets with friendly houses.",
                             item=Item("Neighbour's keys", "a bunch of keys on a ring")),
        "Clinic": Room("Clinic", "The dog clinic. Dog supplies are sold here.", locked=True),
        "Forest": Room("Forest", "A deep, green forest. Somewhere, a dog is waiting."),
    }


class Game:
    """Holds the whole game state: rooms, player and progress flags."""

    def __init__(self, name, age):
        self.rooms = create_rooms()
        # The player starts in the Neighborhood
        self.player = Player(name, age, self.rooms["Neighborhood"])
        self.map_used = False       # has the map been used yet?
        self.keys_returned = False  # has the neighbour got the keys back?
        self.finished = False       # becomes True when Duty is found

    def to_dict(self):
        """Turn the state into a dictionary that can be saved to a file."""
        p = self.player
        return {
            "name": p.name,
            "age": p.age,
            "coins": p.coins,
            "location": p.location.name,
            "items": "|".join(i.name for i in p.items),  # list -> one text
            "clues": "|".join(p.clues),
            "clinic_unlocked": not self.rooms["Clinic"].locked,
            "map_taken": self.rooms["Park"].item is None,
            "keys_taken": self.rooms["Neighborhood"].item is None,
            "map_used": self.map_used,
            "keys_returned": self.keys_returned,
            "finished": self.finished,
        }

    @classmethod
    def from_dict(cls, data):
        """Build a Game from saved data (the opposite of to_dict)."""
        game = cls(data["name"], int(data["age"]))
        p = game.player
        p.coins = int(data["coins"])
        p.move_to(game.rooms[data["location"]])
        # split("|") turns the saved text back into a list
        p.items = [Item(n) for n in data["items"].split("|") if n]
        p.clues = [c for c in data["clues"].split("|") if c]
        game.rooms["Clinic"].locked = data["clinic_unlocked"] != "True"
        # If the hidden items were already taken, remove them from the rooms
        if data["map_taken"] == "True":
            game.rooms["Park"].take_item()
        if data["keys_taken"] == "True":
            game.rooms["Neighborhood"].take_item()
        game.map_used = data["map_used"] == "True"
        game.keys_returned = data["keys_returned"] == "True"
        game.finished = data["finished"] == "True"
        return game

    def save(self):
        """Save the game to the player's save file."""
        files.save_game(self.player.name, self.to_dict())


# ---------- searching ----------

def found_clue(game, place):
    """Give the player a new clue (the Park hint comes first). Returns text."""
    clues = game.player.clues
    # In the Park, give the bench hint first (while the map is still there)
    if place == "Park" and PARK_HINT not in clues and game.rooms["Park"].item:
        clues.append(PARK_HINT)
        return "You found a clue! " + PARK_HINT
    # Otherwise pick a random clue the player does not have yet
    fresh = [c for c in CLUE_POOL if c not in clues]
    if not fresh:
        return "You already know every clue about this place."
    clue = random.choice(fresh)
    clues.append(clue)
    return "You found a clue! " + clue


def search_location(game):
    """Search the current location. The result is random. Returns text."""
    player = game.player
    place = player.location.name
    roll = random.randint(1, 100)  # a random number from 1 to 100
    if roll <= 40:                 # 40% chance: coins
        coins = random.randint(1, 4)
        player.add_coins(coins)
        return f"You found {coins} coin(s)! You now have {player.coins} coins."
    if roll <= 65:                 # 25% chance: a clue
        return found_clue(game, place)
    if roll <= 80 and place in ("Park", "Neighborhood"):  # an empty bottle
        player.collect(Item("Empty bottle", "can be recycled at the Shop"))
        return "You picked up an empty bottle. Keep the place clean!"
    if roll <= 90 and place == "Neighborhood" and player.location.item:  # the keys
        item = player.location.take_item()
        player.collect(item)
        return f"You found {item.name}! Someone must be missing them."
    return "You looked around but found nothing this time. Try again!"


# ---------- special actions (menu option 4) ----------

def check_bench(game):
    """Look under the old bench in the Park (random chance to find the map)."""
    park = game.rooms["Park"]
    if park.item is None:
        return "You already took the map from under the bench."
    if random.random() < 0.5:  # 50% chance each time
        game.player.collect(park.take_item())
        return "You found an Old map under the bench! Use it in the Shop."
    return "You looked under the bench but only found leaves. Try again!"


def sell_bottles(game):
    """Recycle bottles at the Shop for coins."""
    amount = game.player.remove_items("Empty bottle")  # how many were removed
    if amount == 0:
        return "You have no empty bottles. Search the Park or Neighborhood."
    game.player.add_coins(amount * BOTTLE_PRICE)
    return f"You recycled {amount} bottle(s) and earned {amount * BOTTLE_PRICE} coins."


def return_keys(game):
    """Give the neighbour's keys back for a reward."""
    if game.keys_returned:
        return "The neighbour already thanked you. Thank you again!"
    if not game.player.has_item("Neighbour's keys"):
        return "A neighbour is looking for keys. Maybe you can find them."
    game.player.remove_items("Neighbour's keys")
    game.keys_returned = True
    game.player.add_coins(KEYS_REWARD)
    return f"The neighbour is happy! You got {KEYS_REWARD} coins as a thank-you."


def buy_whistle(game):
    """Buy the dog whistle at the Clinic."""
    player = game.player
    if player.has_item("Dog whistle"):
        return "You already have the dog whistle."
    # spend_coins returns False when the player cannot afford it
    if not player.spend_coins(WHISTLE_COST):
        return f"The whistle costs {WHISTLE_COST} coins. You have {player.coins}."
    player.collect(Item("Dog whistle", "calls Duty from far away"))
    return "You bought the dog whistle! Now you can enter the Forest."


def special_action(game):
    """Run the special action of the current location. Returns text."""
    # A dictionary that connects each place to its function
    actions = {"Park": check_bench, "Shop": sell_bottles,
               "Neighborhood": return_keys, "Clinic": buy_whistle}
    action = actions.get(game.player.location.name)
    return action(game) if action else "Everything is quiet here."


def use_map(game):
    """Use the map in the Shop to dig up hidden coins."""
    player = game.player
    if not player.has_item("Old map"):
        return "You do not have a map. Maybe look in the Park?"
    if game.map_used:
        return "You already followed the map."
    if player.location.name != "Shop":
        return "The map shows an X behind the Shop. Go there first."
    game.map_used = True
    player.remove_items("Old map")
    player.add_coins(MAP_BONUS)
    return f"You dug behind the Shop and found a box with {MAP_BONUS} coins!"


# ---------- travelling ----------

def enter_forest(game):
    """Try to enter the Forest. Needs an unlocked Clinic and the whistle."""
    if game.rooms["Clinic"].locked:
        return "The forest path is blocked. First unlock the Clinic (15 coins)."
    if not game.player.has_item("Dog whistle"):
        return "You cannot call Duty without a dog whistle. Buy one at the Clinic."
    # Both rules passed: the player finds Duty and the game ends
    game.player.move_to(game.rooms["Forest"])
    game.finished = True
    return ("You blow the whistle... and hear a happy bark!\n"
            "Duty runs out of the trees and jumps into your arms!")


def travel(game, room_name):
    """Move to a room, handling the locked Clinic. Returns text."""
    room = game.rooms[room_name]
    if room_name == "Forest":
        return enter_forest(game)  # the Forest has its own rules
    if room.locked:
        if game.player.coins < CLINIC_COST:
            return f"The Clinic is locked. You need {CLINIC_COST} coins (you have {game.player.coins})."
        # The player has enough coins, so ask if they want to pay
        answer = input(f"Pay {CLINIC_COST} coins to unlock the Clinic? (y/n): ").strip().lower()
        if answer != "y":
            return "You decide to wait."
        game.player.spend_coins(CLINIC_COST)
        room.locked = False
        game.player.move_to(room)
        return "The Clinic is unlocked! You walk in."
    game.player.move_to(room)
    return f"You walk to the {room.name}. {room.description}"


def explore_random(game):
    """Go to a random location other than the current one."""
    options = [name for name in game.rooms if name != game.player.location.name]
    choice = random.choice(options)  # pick one place at random
    return f"You wander off and end up at: {choice}.\n" + travel(game, choice)
