import random

def roll_custom_dice(sides):
   
    return random.randint(1, sides)

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    
    print(f"Rolling the {sides}-sided dice until we get a {sides}:")
    while True:
        result = roll_custom_dice(sides)
        print(f"Rolled: {result}")
        if result == sides:
            print(f"Found the maximum number ({sides})! Stopping.")
            break

if __name__ == "__main__":
    main()
