# creating while loop, where the user must re-enter the password until the password is correct
password = 123
guess = int(input("enter password: "))

while guess != password:
    print("wrong password, try again")
    guess = int(input("enter password: "))
print("correct password")