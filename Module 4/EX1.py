Size_limit = 42

length = float(input("Enter the length of the zander in centimeters: "))

if length >= Size_limit:
    print("The fish meets the size limit.")
else:
    difference = Size_limit - length
    print("Please release the fish back into the lake.")
    print(f"The fish is {difference:.1f} centimeters below the size limit.")
