# The user enters two numbers, and the program should print the sum of all numbers in that range (using a for loop)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num_sum = 0

for num in range(num1, num2 +1):
    num_sum += num
print("The sum of all numbers from", num1, "to", num2, "is", num_sum)
