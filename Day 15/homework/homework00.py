# Writing a program that asks the user for a number (using input), checks if the number is even, and prints whether it's even or not. 
# If entered number is not even, printing the next even number too.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is not even.", num + 1, "is even")