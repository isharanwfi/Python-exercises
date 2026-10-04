#Player_Name = input("Enter your name: ")
#Player_Age = int(input("Enter your age: "))

#if Player_Age < 12:    
    #print("You are a minor. The game will now shut down.")
#else:

    #print("\nWelcome to CALL OF DUTY!")
    
    #while True:
     
        #print("\nMAIN MENU")
        #print("Available commands:")
        #print("  'status' : Check your player status")
        #print("  'inventory' : Open your backpack")
        #print("  'explore' : Search the surrounding area")
        #print("  'lopeta' : Quit the game")
        #print("-----------------")
      
        #command = input("Enter a command: ").strip().lower()
    
        #if command == "lopeta":
            #print("Thank you for playing CALL OF DUTY! \nGoodbye.")
            #break
            
      
        #elif command == "status":
           # print("\n[CONSOLE] Status: Level 5 ")
        #elif command == "inventory":
            #print("\n[CONSOLE] Inventory: 42x Gold Coins")
        #elif command == "explore":
            #print("\n[CONSOLE] You look around...")
        #else:
           # print(f"\n[CONSOLE] Unknown command: '{command}'. Please try again.")



# ==============================================================
# CALL OF DUTY
# PROJECT 2 - Modify main menu to add more commands and features.
# ==============================================================

# Ask for player's name
Player_Name = input("Enter your name: ")

# Ask for player's age
Player_Age  = int(input("Enter your age: "))


# ==========================================
# AGE CHECK
# ==========================================
if Player_Age < 12:

    print("\nYou are a minor.")
    print("You must be 12 or older to play.")
    print("Game stopped.")

else:

    # Greeting
    print("\nWelcome", Player_Name, "!")
    print("Welcome to CALL OF DUTY!")


    # ==========================================
    # MAIN MENU
    # ==========================================

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
        print("8. lopeta - Exit the game")
        print("================================")

        Choice = int(input("Enter your choice (1-8): "))


        if Choice == 1: 
            print("Explore: \nYou are going to search the surrounding area...")

        elif Choice == 2:
            print("Map: \nYou are going to open the map to know your searching locations...")

        elif Choice == 3:
            print("Inventory: \nYou are going to check your collected items...")

        elif Choice == 4:
            print("Clues: \nYou are going to identify the clues...")

        elif Choice == 5:
            print("Status: \nYou are going to check player's status...")

        elif Choice == 6:           
            print("Save Game: \nYou are going to save your progress...")

        elif Choice == 7:
            print("Instructions: \nYou are going to view game instructions...")

        elif Choice == 8:
            print("Exit Game: \nYou are going to exit the game.... \nThank you for playing CALL OF DUTY! \nGoodbye.")
            break

        else:
            print("Invalid choice! \nPlease enter a number from 1 to 8.")