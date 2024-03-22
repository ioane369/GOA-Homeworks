# doing exercises about for loop and in range() 
                         

# 1) creating a program that prints all the numbers from 1 to 20

for i in range(1, 21):
    print(i)



# 2) creating a program that prints odd numbers from 1 to 20
    
number = -1

for i in range (10):
    number += 2
    print(number, "is odd")



# 3) creating a program that prints square numbers from 1 to 100

for i in range(1, 11):
    print(i * i, "is a perfect square")



# 4) creating a program that calculates sum of all numbers from 1 to 20

number = 1
number_sum = 0    

for i in range(20):
    print(number)
    number_sum += number
    number += 1
print("Sum of all numbers from 1 to 20 is", number_sum) 



# 5) creating program that calculates sum of all even numbers from 1 to 100

number = 2
number_sum = 0

for i in range(50):
    number_sum += number
    number += 2
print("Sum of all even numbers from 1 to 100 is", number_sum)



# 6) creating a program that takes a number as input and prints the multiplication table for that number up to 10

number = int(input("Enter a number: "))
multiplicand = 0

for i in range(1, 11):
    multiplicand += 1
    print(number, "multiplied by", i, "is equal to", number * multiplicand)



# 7) creating a program that takes the word as input and prints letters of it

word = input("Enter the word: ")

print("Letters of word", word, "are: ")
for i in word:
    print(i)



# 8) creating a program that prints factorial of a given number

number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i
print("Factorial of", number, "is", factorial)



# 9) creating a program that prints Fibonacci series up to a certain limit

number = -1
next_number = 1
result = 0

for i in range(int(input("Enter a number: "))):    
    result = number + next_number
    number = next_number
    next_number = result
    print(result)



# 10) creating a program that takes number as input and outputs the sum of the digits of that number

number = input("Enter a number: ")
digit_sum = 0

for digit in number:
    digit_sum += int(digit)
print("Sum of the digits of the", number, "is", digit_sum)