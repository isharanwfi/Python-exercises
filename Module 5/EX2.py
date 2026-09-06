number = True
while number:
    user_input = float(input("Enter inches to convert (or a negative numbers to quit): "))
    if user_input < 0:
        print("Negative value entered.Program ends.")
    else:
        Centimeters = float((user_input) * 2.54)
    print(f"{user_input} inches is equal to {float(Centimeters):.2f} cm\n.")
    
 