smallest = None
largest = None

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    
   
    if user_input == "":
        break
        
    
    num = float(user_input)
    
    
    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num


if smallest is not None:
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No numbers were entered.")