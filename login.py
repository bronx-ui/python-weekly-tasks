username = "student"
password = "python123"

attempts = 3

while attempts > 0:
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username == username and entered_password == password:
        print("Login successful!")
        print("Welcome back.")
        break
    else:
        attempts -= 1
        print("Invalid username or password.")

        if attempts > 0:
            print(f"You have {attempts} attempt(s) left.")
        else:
            print("Too many failed attempts. Access denied.")