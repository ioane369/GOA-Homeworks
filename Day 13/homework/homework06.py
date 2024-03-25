""" Writing a program that prompts the user to enter a number. 
If the number is divisible by 3, it prints "Fizz". If divisible by 5, it prints "Buzz". 
If divisible by both 3 and 5, it prints "FizzBuzz". Otherwise, it prints the number itself   """

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)