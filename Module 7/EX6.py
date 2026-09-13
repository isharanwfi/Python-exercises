import math

def pizza_unit_price(diameter_cm, price_euros):
   
    radius_meters = (diameter_cm / 2) / 100
    
    area_sq_meters = math.pi * (radius_meters ** 2)
    
   
    return price_euros / area_sq_meters

def main():
    print("--- Pizza 1 ---")
    d1 = float(input("Enter diameter in cm: "))
    p1 = float(input("Enter price in euros: "))
    
    print("\n--- Pizza 2 ---")
    d2 = float(input("Enter diameter in cm: "))
    p2 = float(input("Enter price in euros: "))
    
   
    unit_price1 = pizza_unit_price(d1, p1)
    unit_price2 = pizza_unit_price(d2, p2)
    
    print(f"\nPizza 1 unit price: {unit_price1:.2f} €/m²")
    print(f"Pizza 2 unit price: {unit_price2:.2f} €/m²")
    
  
    if unit_price1 < unit_price2:
        print("Pizza 1 provides better value for money!")
    elif unit_price2 < unit_price1:
        print("Pizza 2 provides better value for money!")
    else:
        print("Both pizzas offer the exact same value for money.")

if __name__ == "__main__":
    main()
