# Writing a program that prints all numbers from 1 to 20 that are divisible by both 3 and 5 (using a whie loop)

num = 1

while num <= 20:
    if num % 3 == 0 and num % 5 == 0:
        print(num, "is divisible by both 3 and 5")
    num += 1
    