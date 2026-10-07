"""Classes used by CALL OF DUTY: Item, Room and Player.

A class is a blueprint. An object is one real thing made from a blueprint.
Example: Item("Old map") makes one Item object.
"""


class Item:
    """Something the player can collect, for example a map or a bottle."""

    def __init__(self, name, description=""):
        # __init__ runs automatically when a new Item is created.
        # "self" means "this item itself".
        self.name = name                # for example "Old map"
        self.description = description  # short text, can be empty

    def __str__(self):
        # Decides how the item looks when it is printed.
        return f"{self.name} - {self.description}" if self.description else self.name


class Room:
    """A location in the game world. It may hide one item."""

    def __init__(self, name, description, locked=False, item=None):
        self.name = name                # for example "Park"
        self.description = description  # text shown when the player arrives
        self.locked = locked            # True = player cannot enter yet
        self.item = item                # hidden item, or None if nothing is hidden

    def take_item(self):
        """Remove the hidden item from the room and return it (or None)."""
        found = self.item  # remember the item
        self.item = None   # the room is empty now, so it can be taken only once
        return found


class Player:
    """The player: name, age, coins, items, clues and current location."""

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location  # a Room object: where the player is now
        self.items = []           # list of Item objects the player carries
        self.clues = []           # list of clue texts the player has found
        self.coins = 0            # the player starts with no coins

    def move_to(self, room):
        """Move the player to another room."""
        self.location = room

    def collect(self, item):
        """Add an item to the player's inventory."""
        self.items.append(item)  # append adds to the end of a list

    def has_item(self, name):
        """Return True if the player owns an item with this name."""
        # any(...) is True if at least one item matches
        return any(item.name == name for item in self.items)

    def count_items(self, name):
        """Return how many items with this name the player owns."""
        return sum(1 for item in self.items if item.name == name)

    def remove_items(self, name):
        """Remove all items with this name and return how many were removed."""
        amount = self.count_items(name)
        # keep only the items whose name is different
        self.items = [item for item in self.items if item.name != name]
        return amount

    def add_coins(self, amount):
        """Give the player more coins."""
        self.coins += amount

    def spend_coins(self, amount):
        """Pay coins if the player has enough. Returns True when paid."""
        if self.coins >= amount:
            self.coins -= amount
            return True   # payment worked
        return False      # not enough coins
