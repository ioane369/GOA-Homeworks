# Asking the user for whole number. Then, creating a factorial for this number and printing it out.

num = int(input("Enter a whole number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)