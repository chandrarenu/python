users = {}   # Dictionary to store username and password

# for registration form

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users:
        print("username already exists!")
    else:
        users[username] = password
        print("Registration successful!")

# for login form

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username not in users:
        print("Username not found!")
    elif users[username] != password:
        print("Incorrect password!")
    else:
        print(f"Welcome back, {username}!")
        
running = True
while running:
    print("\n--- Registration and Login System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        running = False
        print("Exiting program.")
    else:
        print("Invalid choice. Please try again.")
  
