talents = float(input("Enter talents:\n "))
pounds = float(input("Enter pounds:\n "))
lots = float(input("Enter lots:\n "))

talents_in_grams = talents * 20 * 32 * 13.3
pounds_in_grams = pounds * 32 * 13.3
lots_in_grams = lots * 13.3

Total_weight_in_grams = talents_in_grams + pounds_in_grams + lots_in_grams

kilograms = int(Total_weight_in_grams // 1000)
grams = float(Total_weight_in_grams % 1000)

print(f"The weight in modern units:{kilograms} kilograms and {grams:.2f} grams  ")