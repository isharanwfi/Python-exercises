numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    
    if user_input == "":
        break    
 
    numbers.append(float(user_input))

numbers.sort(reverse=True)

top_five = numbers[:5]

print("The five greatest numbers are:")

for num in top_five:
    print(num)
