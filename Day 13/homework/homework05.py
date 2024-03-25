# Writing a program that asks the user to enter a number between 1 and 5. If the number is less than 1 or greater than 5,
# program prints "Invalid input". If the number is between 1 and 5, program prints "Valid input".

entered_number = int(input("Entter a number between 1 and 5: "))

if entered_number < 1 or entered_number > 5:
    print("Invalid input")
else:
    print("Valis input")