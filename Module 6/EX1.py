import random


num_dice = int(input("How many dice would you like to roll? "))

total_sum = 0

for i in range(num_dice):
  
    roll = random.randint(1, 6)
    

    total_sum += roll

print(f"The total sum of rolling {num_dice} dice is: {total_sum}")
