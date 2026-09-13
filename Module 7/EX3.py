def gallons_to_liters(gallons):
   
    return gallons * 3.785

def main():
    while True:
        user_input = float(input("Enter gasoline volume in gallons (negative value to quit): "))
        if user_input < 0:
            print("Negative value entered. Exiting program.")
            break
        
        liters = gallons_to_liters(user_input)
        print(f"{user_input} gallons is approximately {liters:.2f} liters.\n")

if __name__ == "__main__":
    main()
