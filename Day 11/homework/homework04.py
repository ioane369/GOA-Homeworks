# Writing a program that simulates a simple login system (using if else)

username = "admin"
password = "password123"

while True:
    entered_username = input("Please enter username: ")

    if entered_username != username:
        print("Invalid username, try again")
    else:
        while True:
            entered_password = input("Please enter password: ")

            if entered_password != password:
                print("wrong password, try again")
            else:
                print("Login successful")
                exit()