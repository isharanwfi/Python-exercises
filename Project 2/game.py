Player_Name = input("Enter your name: ")
Player_Age = int(input("Enter your age: "))

if Player_Age < 12:
    print("You are a minor. The game will now shut down.")
else:

    print("\nWelcome to CALL OF DUTY!")
    
    while True:
     
        print("\nMAIN MENU")
        print("Available commands:")
        print("  'status' : Check your player status")
        print("  'inventory' : Open your backpack")
        print("  'explore' : Search the surrounding area")
        print("  'lopeta' : Quit the game")
        print("-----------------")
      
        command = input("Enter a command: ").strip().lower()
    
        if command == "lopeta":
            print("Thank you for playing CALL OF DUTY! \nGoodbye.")
            break
            
      
        elif command == "status":
            print("\n[CONSOLE] Status: Level 5 ")
        elif command == "inventory":
            print("\n[CONSOLE] Inventory: 42x Gold Coins")
        elif command == "explore":
            print("\n[CONSOLE] You look around...")
        else:
            print(f"\n[CONSOLE] Unknown command: '{command}'. Please try again.")
