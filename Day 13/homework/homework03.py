# Writing a program that asks the user to enter a password. If the password is "abc123", program prints "Access granted"; 
# otherwise, it prints "Access denied"

entered_password = input("Enter a password: ")

if entered_password == "abc123":
    print("Access granted")
else:
    print("Acess denied")