users = {}

while True:
    print("\n--- Registration and Login System ---")
    print("1. Register")
    print("2. Login")
    print("3. Logout")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users:
            print("Username already exists!")
        else:
            users[username] = password
            print("User registered successfully!")
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username not in users:
            print("Username not found!")
        elif users[username] != password:
            print("Incorrect password!")
        else:
            print(f"Welcome , {username}!")
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
