# doing exercises about while loop and if-else statement


# 1) number guessing game

secret_num = 13
guess = False

while guess == False:
    user_guess = input("Guess the number (from 0 to 30): ")
    if int(user_guess) == secret_num:
        guess = True
        print("That's right")
    else:
        print("Try again")



# 2) creating a program that counts even and odd numbers entered by the user

print("Program stops working once you type 0")
even_count = 0
odd_count = 0
num = int(input("Enter a number: "))

while num > 0 == False:
    num = int(input("Enter a number: "))
    if num == 0:
        num > 0 == True
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("number of even numbers is", even_count)
print("number od odd numbers is", odd_count)



# 3) number guessing game with limited attempts (only five attempts)

num = 33
guess = False
attempts = 0

while guess == False and attempts < 5:
    user_guess = int(input("Enter a number (from 1 to 40): "))

    if user_guess == 33:
        guess = True
        print("That's right")
    elif user_guess < num:
        print("higher")
    else:
        print("lower")
    
    attempts += 1



# 4) number range validator

error = False

while error == False:
    num = int(input("Enter a number between 1 and 20: "))
    if num >= 1 and num <= 20:
        print("valid number")
    else:
        print("Invalid number")
        error = True
        


# 5) multiplication table (input should be between 1 and 10, if input is outside this range, program outputs an error)

num = int(input("Enter a number from 1 to 10: "))
multiplicand = 1
error = False

while multiplicand < 10 and error == False:
    answer = num * multiplicand
    if num > 10:
        print("Error, please enter valid number")
        error = True
    else:
        print(num, "multiplied by", multiplicand, "is equal to", answer)
    multiplicand += 1



# 6) factorial calculator (if user inputs non-negative integer, program outputs error)    

num = int(input("Enter non-negative integer: "))

factorial = 1
iteration = 1

if num < 0:
    print("Error")
else:
    while iteration <= num:
        factorial *= iteration
        iteration += 1
    print("Factorial of", num, "is", factorial)



# 7) password checker (user has only 3 attempts)

password = "traqtori123"
acess = False
attempts = 0

while acess == False and attempts < 3:
    attempts += 1
    guess = input("Enter password: ")

    if guess == password:
        print("correct password")
        acess = True
    else:
        print("wrong password, try again")



# 8) creating a program that prints numbers from 1 to 100, but for multiples of 6 it prints "eqvsi" and for multiples of 10
# it prints "ati", for multiples of both 3 and 5 - prints "eqvsiati"

num = 0

while num < 100:
    num += 1
    
    if num % 6 == 0 and num % 10 == 0:
        print("eqvsiati")
    elif num % 6 == 0:
        print("eqvsi")
    elif num % 10 == 0:
        print("ati")
    else:
        print(num)   



# 9) word guessing game, after each letter program tells user if letter is correct or not

secret_word = "name"

print("Guess the word: what is something that we all have, but we don't get to choose ? (consists of 4 letters)")

first_guess = False

while first_guess == False:
    first_letter = input("Enter first letter: ")

    if first_letter == "n":
        print("correct letter")
        first_guess = True
    else:
        print("wrong letter")

second_guess = False

while second_guess == False:
    second_letter = input("Enter second letter: ")
    
    if second_letter == "a":
        print("correct letter")
        second_guess = True
    else:
        print("wrong letter")
    third_guess = False

while third_guess == False:    
    third_letter = input("Enter third letter: ")

    if third_letter == "m":
        print("correct letter")
        third_guess = True
    else:
        print("wrong letter")

    last_guess = False

while last_guess == False:
    last_letter = input("Enter last letter: ")

    if last_letter == "e":
        print("correct letter, the secret word was name")
        last_guess = True

    else:
        print("wrong letter")
    


# 10) creating a program that determines absolute value of a number (user can enter only 5 numbers)

enters = 0

while enters < 5:
    num = int(input("Enter a number: "))
    enters += 1

    if num < 0:
        absolute_value = - num
        print("absolute value of", num, "is", absolute_value)
    else:
        print("absolute value of", num, "is", num)