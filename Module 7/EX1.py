import random

def roll_dice():
   
    return random.randint(1, 6)

def main():
    print("Rolling the 6-sided dice until we get a 6:")
    while True:
        result = roll_dice()
        print(f"Rolled: {result}")
        if result == 6:
            print("Found a 6! Stopping.")
            break

if __name__ == "__main__":
    main()


  