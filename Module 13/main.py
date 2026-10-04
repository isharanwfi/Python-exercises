# ==========================================
# CALL OF DUTY - LOST DOG
# ==========================================

player_name = ""
player_age = 0

clues = 0
dog_whistle = False
max_found = False

inventory = []


# ==========================================
# INTRODUCTION
# ==========================================

def show_intro():

    with open("intro.txt", "r") as file:
        intro = file.read()

    print(intro)


# ==========================================
# INSTRUCTIONS
# ==========================================

def show_instructions():

    with open("instructions.txt", "r") as file:
        instructions = file.read()

    print(instructions)


# ==========================================
# SAVE GAME
# ==========================================

def save_game():

    with open("savegame.txt", "w") as file:

        file.write(player_name + "\n")
        file.write(str(player_age) + "\n")
        file.write(str(clues) + "\n")
        file.write(str(dog_whistle) + "\n")
        file.write(str(max_found) + "\n")
        file.write(",".join(inventory))

    print("\nGame saved successfully!")


# ==========================================
# LOAD GAME
# ==========================================

def load_game():

    global player_name
    global player_age
    global clues
    global dog_whistle
    global max_found
    global inventory

    try:

        with open("savegame.txt", "r") as file:

            player_name = file.readline()
            player_age = int(file.readline())
            clues = int(file.readline())

            dog_whistle = file.readline().strip() == "True"
            max_found = file.readline().strip() == "True"

            inventory_line = file.readline()

            if inventory_line:
                inventory = inventory_line.split(",")
            else:
                inventory = []

        print("\nGame loaded successfully!")

    except FileNotFoundError:

        print("\nNo saved game found.")


# ==========================================
# START GAME
# ==========================================

show_intro()

show_instructions()


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n================================")
    print("          MAIN MENU")
    print("================================")
    print("park      - Go to the park")
    print("shop      - Visit the shop")
    print("forest    - Go to the forest")
    print("inventory - Check inventory")
    print("status    - Check status")
    print("save      - Save game")
    print("load      - Load game")
    print("help      - Show instructions")
    print("lopeta    - Exit game")
    print("================================")

    command = input("Enter command: ")

    if command == "park":

        print("\nYou go to the park.")

    elif command == "shop":

        print("\nYou visit the shop.")

    elif command == "forest":

        print("\nYou enter the forest.")

    elif command == "inventory":

        print("\nInventory:", inventory)

    elif command == "status":

        print("\nClues:", clues)
        print("Dog whistle:", dog_whistle)
        print("Duty found:", max_found)

    elif command == "save":

        save_game()

    elif command == "load":

        load_game()

    elif command == "help":

        show_instructions()

    elif command == "lopeta":

        print("\nThank you for playing!")
        break

    else:

        print("\nUnknown command. Type 'help' for instructions.")