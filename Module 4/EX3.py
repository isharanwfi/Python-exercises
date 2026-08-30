gender = input("Enter biological gender (male/female): ").lower()
HB_value = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if HB_value < 117:
        print("Hemoglobin value is low.")
    elif HB_value <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
elif gender == "male":
    if HB_value < 134:
        print("Hemoglobin value is low.")
    elif HB_value <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender entered.")
