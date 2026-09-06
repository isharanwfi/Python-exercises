import random

draw_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess > draw_number:
        print("Too high")
    elif guess < draw_number:
        print("Too low")
    else:
        print("Correct!")
        break  