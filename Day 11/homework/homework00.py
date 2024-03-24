# 1) writing a program that takes an input from the user and checks if it's positive, negative or 0 (using if else)

num = float(input("Enter a number: "))

if num < 0:
    print(num, "is negative")
elif num == 0:
    print(num, "is 0")
else:
    print(num, "is positive")