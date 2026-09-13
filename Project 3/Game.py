
inventory = []

def add_item():
  
    item = input("Enter the name of the item to add to your inventory: ").strip()
    if item:
        inventory.append(item)
        print(f" {item} has been safely stowed in your inventory.")
    else:
        print("Cannot add an empty item name.")

def print_inventory():
   
    print("\n--- Current Inventory Items ---")
    if not inventory:
        print("[Your inventory bag is currently empty]")
    else:
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")
    print("--------------------------------")

def discard_item():
   
    if not inventory:
        print(" Nothing to discard. Inventory is already empty.")
        return
        
    print_inventory()
    item_to_remove = input("Enter the name of the item you want to drop: ").strip()
    
    if item_to_remove in inventory:
        inventory.remove(item_to_remove)
        print(f" Dropped {item_to_remove} from your inventory.")
    else:
        print(f"{item_to_remove} was not found in your inventory.")

def main():
    while True:
        print("\n=== GAME MAIN MENU ===")
        print("1. Add Item to Inventory")
        print("2. View Inventory Bag")
        print("3. Discard Item")
        print("4. Exit Game")
        
        choice = input("Select an action (1-4): ").strip()
        
        if choice == "1":
            add_item()
        elif choice == "2":
            print_inventory()
        elif choice == "3":
            discard_item()
        elif choice == "4":
            print("Saving state... Exiting the game. Thank you for playing!")
            break
        else:
            print("Invalid selection. Choose a valid menu action.")

if __name__ == "__main__":
    main()
