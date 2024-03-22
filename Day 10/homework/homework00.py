# creating a program where the user enters the password until the entered password matches the registered one 
# (using while loop and if else)

registered_password = 12345
access = False

while access == False:
    entered_password = int(input("Enter password: "))

    if entered_password == registered_password:
         print("Correct password, access granted ")
         access = True
    else:
         print("Wrong password, try again") 