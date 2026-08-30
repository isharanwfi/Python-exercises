import random


digit1_3 = random.randint(0,9) 
digit2_3 = random.randint(0,9)
digit3_3 = random.randint(0,9)

code_3digit = f"{digit1_3}{digit2_3}{digit3_3}"


digit1_4= random.randint(1,6)    
digit2_4 = random.randint(1,6)
digit3_4 = random.randint(1,6)
digit4_4 = random.randint(1,6)

code_4digit = f"{digit1_4}{digit2_4}{digit3_4}{digit4_4}"

print(f"The 3-digit code: {code_3digit}\nThe 4-digit code: {code_4digit}")