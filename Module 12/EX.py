# ==============================================================
# CALL OF DUTY
# Module 12- Organize the Structure and Introduce Objects
# ==============================================================

from random import choice
import sys

# ==========================================
# OBJECT CLASSES (OOP STRUCTURE)s
# ==========================================

class Item:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Room:
    def __init__(self, name: str, item: Item = None, coins_reward: int = 0, clues_reward: int = 0, requires_unlock: bool = False, unlock_cost: int = 0):
        self.name = name
        self.item = item
        self.coins_reward = coins_reward
        self.clues_reward = clues_reward
        self.requires_unlock = requires_unlock
        self.unlock_cost = unlock_cost
        self.is_unlocked = not requires_unlock
        self.searched_for_clues = False

    def remove_item(self):
        """Removes and returns the item from the room if present."""
        extracted_item = self.item
        self.item = None
        return extracted_item


class Player:
    def __init__(self, name: str, age: int, starting_location: Room):
        self.name = name
        self.age = age
        self.items = []        # List containing Item objects owned by the player
        self.location = starting_location
        self.coins = 0
        self.clues_found = 0

    def move(self, destination: Room):
        """Changes the player's current room location."""
        self.location = destination
        print(f"\nYou traveled to the {destination.name}.")

    def collect_item(self):
        """Picks up an item from the current room if available."""
        room = self.location
        if room.item:
            picked_item = room.remove_item()
            self.items.append(picked_item)
            print(f"\nYou found a {picked_item.name}! Added to your inventory.")
        else:
            print("\nYou search around, but there are no items left to pick up here.")

    def has_item(self, item_name: str) -> bool:
        """Helper to quickly check if player owns a specific item name."""
        return any(item.name.lower() == item_name.lower() for item in self.items)


# ==========================================
# GAME INITIALIZATION
# ==========================================

# 1. Create items
map_item = Item(name="Map")
whistle_item = Item(name="Dog Whistle")

# 2. Create rooms with specific rewards and states
park = Room("Park", item=map_item, coins_reward=5, clues_reward=1)
shop = Room("Shop", coins_reward=10, clues_reward=2)
neighborhood = Room("Neighborhood", coins_reward=10, clues_reward=2)
clinic = Room("Clinic", item=whistle_item, requires_unlock=True, unlock_cost=15)
forest = Room("Forest")
main_menu_hub = Room("Main Menu Hub")

# Map mapping number choices to Room objects
world_map = {
    1: park,
    2: shop,
    3: neighborhood,
    4: clinic,
    5: forest
}

# 3. Setup Player
print("==============================================================")
print("             WELCOME TO CALL OF DUTY: PROJECT 4               ")
print("==============================================================")
player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

player = Player(name=player_name, age=player_age, starting_location=main_menu_hub)


# ==========================================
# CORE GAME MENU FUNCTIONS
# ==========================================

def explore_menu():
    while True:
        print("\n================================")
        print("           EXPLORE")
        print("================================")
        print("1. Park")
        print("2. Shop")
        print("3. Neighborhood")
        print("4. Clinic")
        print("5. Forest")
        print("6. Back to Main Menu")
        print("================================")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Please enter a valid numeric option.")
            continue

        if choice == 6:
            player.location = main_menu_hub
            break

        if choice not in world_map:
            print("\nInvalid choice! Please enter a number from 1 to 6.")
            continue

        target_room = world_map[choice]

        # Handle Room Locks
        if target_room.requires_unlock and not target_room.is_unlocked:
            print(f"\n================================")
            print(f"         4. {target_room.name.upper()}")
            print(f"================================")
            print(f"You need {target_room.unlock_cost} coins to unlock the {target_room.name}.")
            print(f"Your current balance: {player.coins} coins.")
            
            if player.coins >= target_room.unlock_cost:
                unlock = input(f"Unlock {target_room.name.lower()} now for {target_room.unlock_cost} coins? (yes/no): ").lower()
                if unlock == 'yes':
                    player.coins -= target_room.unlock_cost
                    target_room.is_unlocked = True
                    print(f"{target_room.name} has been successfully unlocked!")
                    player.move(target_room)
                else:
                    continue
            else:
                print("Locked! Explore other areas to find more coins first.")
                continue
        else:
            player.move(target_room)

        # Room Specific Logic Routes
        if player.location == park:
            handle_park()
        elif player.location == shop or player.location == neighborhood:
            handle_standard_rewards()
        elif player.location == clinic:
            handle_clinic()
        elif player.location == forest:
            handle_forest()


# ==========================================
# SUB-LOCATION HANDLERS
# ==========================================

def handle_park():
    while True:
        print("\n================================")
        print("            1. PARK")
        print("================================")
        print("1. Search surrounding area")
        print("2. Search old bench")
        print("3. Back to Explore")
        print("================================")

        try:
            park_choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            continue

        if park_choice == 1:
            print("\nYou search around the park area...")
            if not park.searched_for_clues:
                print(f"You found a clue!")
                print(f"You earned {park.coins_reward} coins!")
                player.clues_found += park.clues_reward
                player.coins += park.coins_reward
                park.searched_for_clues = True
            else:
                print("You've already cleared this area of clues.")

        elif park_choice == 2:
            print("\nYou walk towards the old bench and peer underneath...")
            if park.item is not None:
                player.collect_item()
            else:
                print("You already found the Map here.")

        elif park_choice == 3:
            break
        else:
            print("Invalid choice!")


def handle_standard_rewards():
    room = player.location
    print(f"\n================================")
    print(f"         {room.name.upper()}")
    print(f"================================")
    print(f"You search inside the {room.name.lower()}...")
    
    if not room.searched_for_clues:
        print(f"You found {room.clues_reward} clues!")
        print(f"You earned {room.coins_reward} coins!")
        player.clues_found += room.clues_reward
        player.coins += room.coins_reward
        room.searched_for_clues = True
    else:
        print("You've already thoroughly explored this location.")


def handle_clinic():
    room = player.location
    print(f"\n================================")
    print(f"         4. CLINIC")
    print(f"================================")
    print("You are managing the Clinic...")
    print(f"Your current balance: {player.coins} coins.")
    
    if room.item is not None:
        buy_choice = input(f"Would you like to buy a {room.item.name} for 5 coins? (yes/no): ").lower()
        if buy_choice == 'yes':
            if player.coins >= 5:
                player.coins -= 5
                player.collect_item()
                print(f"Your remaining balance: {player.coins} coins.")
            else:
                print("You do not have enough coins to purchase the whistle!")
    else:
        print("You already bought the Dog Whistle. There is nothing else to buy.")


def handle_forest():
    print(f"\n================================")
    print(f"         5. FOREST")
    print(f"================================")
    print("You are exploring the deep Forest...")
    print("Checking your Inventory...")
    
    if player.has_item("Dog Whistle"):
        print("\nYou blew the Dog Whistle! You successfully called DUTY!")
        print("Congratulations! You completed the mission!")
        print("Thanks for playing! Game will now exit.")
        sys.exit()
    else:
        print("\nThe forest is deep and dangerous. You can proceed if you have a Dog Whistle to call DUTY.")


# ==========================================
# AUXILIARY SYSTEM INTERFACES
# ==========================================

def view_map():
    print("\n================================")
    print("           VIEW MAP")
    print("================================")
    print("You opened the map.")
    print("Searching locations:")
    print("1. Park         : Contains an item check")
    print("2. Shop         : Provides coins and clues")
    print("3. Neighborhood : Provides coins and clues")
    print(f"4. Clinic       : [{'Unlocked' if clinic.is_unlocked else 'Locked: Requires 15 coins'}]")
    print("5. Forest       : End-Game Mission Zone (Requires Dog Whistle)")
    print("================================")


def inventory_menu():
    while True:
        print("\n================================")
        print("          INVENTORY")
        print("================================")
        print("1. Add custom item manually")
        print("2. View Inventory Details")
        print("3. Back to Main Menu")
        print("================================")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("\nInvalid input. Please type a number.")
            continue
            
        if choice == 1:
            item_name = input("\nEnter the item name you found: ")
            new_item = Item(item_name)
            player.items.append(new_item)
            print(f"\n{new_item.name} has manually been added to your inventory.")
            
        elif choice == 2:
            print("\n================================")
            print("          VIEW INVENTORY")
            print("================================")
            if len(player.items) == 0:
                print("Your inventory is empty.")
            else:
                print("Your collected items:")
                for inventory_item in player.items:
                    print(f"- {inventory_item}")
            print("================================")
            
        elif choice == 3:
            return


def view_clues():
    print("\n================================")
    print("            CLUES")
    print("================================")
    if player.clues_found == 0:
        print("No clues found yet. Go explore the town!")
    else:
        print(f"Total Clues Identified: {player.clues_found}")
    print("================================")


def view_status():
    print("\n================================")
    print("          PLAYER STATUS")
    print("================================")
    print(f"Player Name:   {player.name}")
    print(f"Player Age:    {player.age}")
    print(f"Total Coins:   {player.coins}")
    print(f"Clues Found:   {player.clues_found}")
    print(f"Current Room:  {player.location.name if player.location != main_menu_hub else 'Main Hub'}")
    print("================================")


# ==========================================
# MAIN GAME EXECUTION LOOP
# ==========================================
while True:
    print("\n================================")
    print("           MAIN MENU")
    print("================================")
    print("1. Explore")
    print("2. View Map")
    print("3. Inventory")
    print("4. View Clues")
    print("5. View Status")
    print("6. Exit Game")
    print("================================")
    
    try:
        main_choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("\nInvalid input. Please type a number.")
        continue
        
    if main_choice == 1:
        explore_menu()
    elif main_choice == 2:
        view_map()
    elif main_choice == 3:
        inventory_menu()
    elif main_choice == 4:
        view_clues()
    elif main_choice == 5:
        view_status()
    elif main_choice == 6:
        print(f"\nThanks for playing, {player.name}! Goodbye.")
        break
    else:
        print("\nInvalid choice! Please select between 1 and 6.")
