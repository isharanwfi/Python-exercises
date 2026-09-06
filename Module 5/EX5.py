CORRECT_USER = "python"
CORRECT_PASSWORD = "rules"

attempts = 0
max_attempts = 5
authenticated = False

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == CORRECT_USER and password == CORRECT_PASSWORD:
        print("Welcome")
        authenticated = True
        break
    else:
        attempts += 1
        print(f"Incorrect credentials. Attempts remaining: {max_attempts - attempts}\n")


if not authenticated:
    print("Access denied")