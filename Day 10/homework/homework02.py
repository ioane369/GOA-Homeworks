# doing exercises about while loop


# 1) creating a program that prints all numbers from 1 to entered bumber

num = 1

while num <= 20:
    print(num)
    num += 1



# 2) creating a program that prints odd numbers from 1 to 30
    
num = 1

while num <= 20:
    print(num, "is odd")
    num += 2



# 3) creating a program that prints square numbers from 100 to 150

num = 10

while num <= 12:
    print(num * num, "is a perfect square")
    num += 1



# 4) creating program that prints sum of all numbers from 50 to 100
    
num = 50
num_sum = 0

while num <= 100:
    num_sum += num
    num += 1
print("sum of all numbers from 50 to 100 is", num_sum,)



# 5) creating a program that prints sum of all odd numbers from 50 to 100

num = 51
num_sum = 0

while num <= 100:
    num_sum += num
    num += 2
print("Sum of all the odd numbers from 50 to 100 is", num_sum)



# 6) creating a program that takes a number as input and prints the multiplication table for that number up to 15

num = int(input("Enter a number: "))
multiplicand = 1

while multiplicand <= 15:
    answer = num * multiplicand
    print(num, "multiplied by", multiplicand, "is equal to", answer)
    multiplicand += 1



# 7) creating a program that prints factorial of a given number

num = int(input("Enter a number: "))
factorial = 1
iteration = 1

while iteration <= num:
    factorial *= iteration
    iteration += 1
print("Factorial of", num, "is", factorial)



# 8) creating a program that prints Fibonacci series up to a certain limit

number = -1
next_number = 1
result = 0
range = int(input("Enter a number: "))
iteration = 1

while iteration <= range:
    result = number + next_number
    number = next_number
    next_number = result
    print(result)
    iteration += 1



# 9) creating a program that prints numbers from first inputed number to second inputed number

start = int(input("Enter first number: "))
finish = int(input("Enter second number: "))

while start <= finish:
    print(start)
    start += 1 


           
# 10) creating a program that prints product of all the even numbers from first input to second input
    
start = int(input("Enter first number (it should be even): "))
finish = int(input("Enter second number: "))
product = 1

while start <= finish:
    product *= start
    start += 2
print("product of all the even numbers in selected range is", product)