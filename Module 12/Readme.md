# Software 1 - Python exercises
**Ishara Nushangani**
## Module 12
I completed exercises 1 and 2


## My Text Adventure Game (Call of Duty)

This project changes our old game code from Project 3 into an **Object-Oriented Programming (OOP)** design.


## (Classes)

### 1. The `Item` Class (Things you can pick up)
This is a simple template used to create items in the game world, like a **Map** or a **Dog Whistle**.
* **(Attributes):** 
  * `name`: The name of the item.

### 2. The `Room` Class (Places you can visit)
This is a template for the different locations in the town (like the Park, Shop, Clinic, or Forest).
* **(Attributes):** 
  * `name`: The name of the location.
  * `item`: The item sitting on the floor inside this room.
  * `coins_reward`: How many coins you get when you search here.
  * `clues_reward`: How many clues you find here.
  * `requires_unlock`: True or False (Does it need to be unlocked first?).
  * `unlock_cost`: The price in coins to unlock the room.
  * `is_unlocked`: True or False (Is the room open right now?).
  * `searched_for_clues`: Remembers if you already took the coins/clues from this room.

* **(Methods):**
  * `remove_item()`: Safely picks up the item from the floor and leaves the floor empty so you cannot copy the item twice.

### 3. The `Player` Class (All about YOU!)
This template tracks everything about the person playing the game.
* **(Attributes):**
  * `name`: The player's name.
  * `age`: The player's age.
  * `items`: A backpack list holding all the Item objects you collected.
  * `location`: The actual Room object you are standing in right now.
  * `coins`: How much money you have.
  * `clues_found`: How many clues you have gathered.
* **(Methods):**
  * `move()`: Changes your location to a new room.
  * `collect_item()`: Takes the item out of the room and puts it inside your backpack list.
  * `has_item()`: Checks your backpack to see if you own a specific item (like checking for the Whistle when you enter the Forest).

## 🔄 The Game Menus & Safety Features

* **`explore_menu()`**: The movement menu. It checks if rooms like the Clinic are locked, checks your wallet to see if you have enough coins to unlock them, and lets you walk around.
* **`inventory_menu()`**: Your backpack manager. It lets you check your items or even type in a name to create a custom item yourself.
* **`try / except` Safety Net**: Stops the game from breaking! If the player accidentally types a word (like "three") instead of a number (like "3"), this safety feature catches the mistake, prints an error message, and lets the student keep playing smoothly.
* **`sys.exit()` Win Trigger**: Used when you enter the Forest with the Dog Whistle. It finishes the story, congratulates you, and closes the game window safely.
