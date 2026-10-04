
#inventory = []

#def add_item():
  
    #item = input("Enter the name of the item to add to your inventory: ").strip()
    #if item:
        #inventory.append(item)
        #print(f" {item} has been safely stowed in your inventory.")
    #else:
        #print("Cannot add an empty item name.")

#def print_inventory():
   
    #print("\n--- Current Inventory Items ---")
    #if not inventory:
        #print("[Your inventory bag is currently empty]")
    #else:
        #for index, item in enumerate(inventory, start=1):
            #print(f"{index}. {item}")
    ##print("--------------------------------")

#def discard_item():
   
    #if not inventory:
        #print(" Nothing to discard. Inventory is already empty.")
        #return
        
    #print_inventory()
    #item_to_remove = input("Enter the name of the item you want to drop: ").strip()
    
    #if item_to_remove in inventory:
        #inventory.remove(item_to_remove)
        #print(f" Dropped {item_to_remove} from your inventory.")
    #else:
        #print(f"{item_to_remove} was not found in your inventory.")

#def main():
    #while True:
        #print("\n=== GAME MAIN MENU ===")
       # print("1. Add Item to Inventory")
        #print("2. View Inventory Bag")
        #print("3. Discard Item")
        #print("4. Exit Game")
        
        #choice = input("Select an action (1-4): ").strip()
        
        #if choice == "1":
            #add_item()
        #elif choice == "2":
            #print_inventory()
        #elif choice == "3":
            #discard_item()
        #elif choice == "4":
            #print("Saving state... Exiting the game. Thank you for playing!")
            #break
        #else:
            #print("Invalid selection. Choose a valid menu action.")

#if __name__ == "__main__":
    #main()

# ==============================================================
# CALL OF DUTY
# PROJECT 3 - Modify Main Menu Functions and “Inventory”.
# ==============================================================

# Global Game Variables to track progress
coins = 0
clues_found = 0
clinic_unlocked = False
inventory = []

# Ask for player's name
Player_Name = input("Enter your name: ")

# Ask for player's age
Player_Age  = int(input("Enter your age: "))


# ==========================================
# 1. EXPLORE FUNCTION
# ==========================================
def explore():
    global coins, clues_found, clinic_unlocked
    
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

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            print("\n================================")
            print("            1. PARK")
            print("================================")
            print("1. Search surrounding area")
            print("2. Search old bench")
            print("3. Back to Explore")
            print("================================")

            park_choice = int(input("Enter your choice (1-3): "))

            if park_choice == 1:
                print("\nYou are exploring the Park...")
                print("You search around the park.")
                print("You found a clue!")
                print("You earned 5 coins!")
                clues_found += 1
                coins += 5

            elif park_choice == 2:
                print("\nYou walk towards the old bench...")
                print("You search under the bench.")
                if "Map" not in inventory:
                    print("You found a Map! Added to inventory.")
                    inventory.append("Map")
                else:
                    print("You already found the Map here.")

            elif park_choice == 3:
                continue
            else:
                print("Invalid choice!")

        elif choice == 2:
            print("\n================================")
            print("             SHOP")
            print("================================")
            print("\nYou are exploring the Shop...")
            print("You search inside the shop.")
            print("You found two clues!")
            print("You earned 10 coins!")
            clues_found += 2
            coins += 10
            
        elif choice == 3:
            print("\n================================")
            print("         3. NEIGHBORHOOD")
            print("================================")
            print("\nYou are exploring the Neighborhood...")
            print("You search around the neighborhood.")
            print("You found two clues!")
            print("You earned 10 coins!")
            clues_found += 2
            coins += 10

        elif choice == 4:
            print("\n================================")
            print("         4. CLINIC")
            print("================================")
            print("You are managing the Clinic...")
            print(f"Your current balance: {coins} coins.")
            
            if clinic_unlocked:
                print("The clinic is already unlocked!")
                if "Dog Whistle" not in inventory:
                    buy_choice = input("Would you like to buy a Dog Whistle for 5 coins? (yes/no): ").lower()
                    if buy_choice == 'yes':
                        if coins >= 5:
                            coins -= 5  # Deducts 5 coins for whistle
                            inventory.append("Dog Whistle")
                            print("Success! You purchased a Dog Whistle.")
                            print(f"Your remaining balance: {coins} coins.")
                        else:
                            print("You do not have enough coins to purchase the whistle!")
                else:
                    print("You already have the Dog Whistle.")
            else:
                print("You need 15 coins to unlock the clinic.")
                if coins >= 15:
                    unlock = input("Unlock clinic now for 15 coins? (yes/no): ").lower()
                    if unlock == 'yes':
                        coins -= 15  # Deducts 15 coins to unlock
                        clinic_unlocked = True
                        print("Clinic has been successfully unlocked!")
                        print(f"Your remaining balance: {coins} coins.")
                        print("Now you can re-enter this menu to purchase the Dog Whistle.")
                else:
                    print("Locked! Explore other areas to find more coins first.")
                        
        elif choice == 5:
            print("\n================================")
            print("         5. FOREST")
            print("================================")
            print("\nYou are exploring the Forest...")
            print("Checking your Inventory...")
            if "Dog Whistle" in inventory:
                print("You blew the Dog Whistle! You successfully called DUTY!")
                print("Congratulations! You completed the mission!")
            else:
                print("The forest is deep and dangerous. You can proceed if you have a Dog Whistle to call DUTY.")

        elif choice == 6:
            return
        else:
            print("\nInvalid choice!")
            print("Please enter a number from 1 to 6.")


# ==========================================
# 2. MAP FUNCTION
# ==========================================
def view_map():
    print("\n================================")
    print("           VIEW MAP")
    print("================================")
    print("You opened the map.")
    print("Searching locations:")
    print("1. Park")
    print("2. Shop")
    print("3. Neighborhood")
    print("4. Clinic (Requires 15 coins to unlock)")
    print("5. Forest (Requires Dog Whistle to complete)")
    print("================================")


# ==========================================
# 3. INVENTORY FUNCTIONS
# ==========================================
def add_inventory():
    item = input("\nEnter the item you found: ")
    inventory.append(item)
    print(f"\n{item} has been added to your inventory.")

def view_inventory():
    print("\n================================")
    print("          VIEW INVENTORY")
    print("================================")
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("Your collected items:")
        for item in inventory:
            print("-", item)
    print("================================")

def inventory_menu():
    while True:
        print("\n================================")
        print("          INVENTORY")
        print("================================")
        print("1. Add item to Inventory")
        print("2. View Inventory")
        print("3. Back to Main Menu")
        print("================================")

        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            add_inventory()
        elif choice == 2:
            view_inventory()
        elif choice == 3:
            return
        else:
            print("\nInvalid choice!")
            print("Please enter a number from 1 to 3.")


# ==========================================
# 4. CLUES FUNCTION
# ==========================================
def view_clues():
    print("\n================================")
    print("            CLUES")
    print("================================")
    if clues_found == 0:
        print("No clues found yet. Go explore the town!")
    else:
        print(f"Total Clues Identified: {clues_found}")
    print("================================")


# ==========================================
# 5. STATUS FUNCTION
# ==========================================
def view_status():
    print("\n================================")
    print("         PLAYER STATUS")
    print("================================")
    print(f"Player Name : {Player_Name}")
    print(f"Player Age  : {Player_Age}")
    print(f"Coins       : {coins}")
    print(f"Clues Found : {clues_found}")
    print(f"Clinic State: {'Unlocked' if clinic_unlocked else 'Locked'}")
    print("================================")


# ==========================================
# AGE CHECK & MAIN GAME LOOP
# ==========================================
if Player_Age < 12:
    print("\nYou are a minor.")
    print("You must be 12 or older to play.")
    print("Game stopped.")
else:
    print("\nWelcome", Player_Name, "!")
    print("Welcome to CALL OF DUTY!")

    while True:
        print("\n================================")
        print("       MAIN MENU")
        print("================================")
        print("1. Explore - search the surrounding area")
        print("2. Map - Open the map to know your searching locations")
        print("3. Inventory - Check your collected items")
        print("4. Clues - Identify the clues")
        print("5. Status - Check player's status")
        print("6. Save Game - Save your progress")
        print("7. Instructions - View game instructions")
        print("8. Lopeta - Exit the game")
        print("================================")

        Choice = int(input("Enter your choice (1-8): "))
   
        if Choice == 1: 
            explore()
        elif Choice == 2:
            view_map()
        elif Choice == 3:
            inventory_menu()
        elif Choice == 4:
            view_clues()
        elif Choice == 5:
            view_status()
        elif Choice == 6: 

            print("\nSave Game: Progress saved successfully!")

        elif Choice == 7:
            print("\nInstructions: Gather clues and coins by exploring. Use coins to unlock the Clinic and buy a Whistle to win in the Forest!")

        elif Choice == 8:
            print("\nThank you for playing CALL OF DUTY! \nGoodbye.")

        break

    else:
        print("Invalid choice! \nPlease enter a number from 1 to 8.")
   
