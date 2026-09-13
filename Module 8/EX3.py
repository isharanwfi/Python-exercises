def main():
   
    airports = {}
    
    while True:
        print("\n--- Airport Database Menu ---")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            icao = input("Enter the ICAO code: ").strip().upper()
            name = input("Enter the airport name: ").strip()
            airports[icao] = name
            print(f"Airport '{name}' ({icao}) successfully added!")
            
        elif choice == "2":
            icao = input("Enter the ICAO code to look up: ").strip().upper()
            if icao in airports:
                print(f"The airport name is: {airports[icao]}")
            else:
                print("Error: Airport code not found in the database.")
                
        elif choice == "3":
            print("Exiting database program. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
