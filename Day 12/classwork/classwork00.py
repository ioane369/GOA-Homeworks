# The user enters 2 numbers, and the program should print all the numbers in that range (using a for loop)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Numbers from", num1, "to", num2, "are:")
for num in range(num1, num2 + 1):
    print(num)