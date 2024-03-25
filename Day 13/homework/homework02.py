# Writing a program that asks the user to enter a number and then prints whether the number is positive, negative, or zero
# (using an if-else statement)

num = float(input("Enter a number: "))

if num < 0:
    print(num, "is negative")
elif num == 0:
    print(num, "is zero")
else:
    print(num, "is positive")