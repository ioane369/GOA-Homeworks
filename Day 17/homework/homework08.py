#                                             WORKING ON FUNCTIONS

# 1) Creating a function that calculates the factorial of a given number.

def factorial(number):
    factorial = 1
    for num in range(1, number + 1):
        factorial *= num
    return factorial

number = int(input("Enter a number: "))
print(factorial(number))



# 2) Writing a function that checks if a given string is a palindrome.

def palindrome_checker(string):
    reversed_string = string[: : -1]
    if reversed_string == string:
        return(string, "is palindrome")
    else:
        return(string, "is not palindrome")

given_string = input("Enter a text: ")
print(palindrome_checker(given_string))



# 3) Defining a function that calculates the sum of squares for a given list of numbers.

def sum_of_squares(numbers):
    squares_sum = 0
    for num in numbers:
        num *= num
        squares_sum += num
    return squares_sum

numbers = [1, 2, 3, 4, 5]

print(sum_of_squares(numbers))



# 4) Creating a function that determines if a given number is prime.

def prime_checker(number):
    division_without_reminder = 0
    for i in range(1, number + 1):
        if number % i == 0:
            division_without_reminder += 1
    if division_without_reminder == 2:
        return number, "is prime"
    else:
        return number, "is not prime"

entered_number = int(input("Enter a number: "))
print(prime_checker(entered_number))



# 5) User enters starting and ending numbers, function adds all the prime numbers in that range, in the new list and then returns the list.

def prime_filter(start, end):
    prime_list = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list

start_num = int(input("Enter the starting number: ")) 
end_num = int(input("Enter the ending number: "))

print("Prime numbers in entered range are:", prime_filter(start_num, end_num))



# 6)  Defining a function that generates the Fibonacci sequence up to a specified number of terms.

def Fibonacci_sequence(number):
    first_num = -1
    second_num = 1
    next_num = 0
    Fibonacci = []
    for i in range(number):
        next_num = first_num + second_num
        first_num = second_num
        second_num = next_num
        Fibonacci.append(next_num)
    return Fibonacci

number_of_series = int(input("Enter a number: "))
print(Fibonacci_sequence(number_of_series))



# 7) Writing a function that takes a user's name and surname as input and returns a personalized welcome message. 

def greeting(name, surname):
    return "Welcome", name, surname

name = input("Enter your name: ")
surname = input("Enter your surname: ")

print(greeting(name, surname))



""" 8) Writing a function that takes a password as input and 
checks its strength based on its length and 
returns a message indicating the strength of the password.   """

def password_strength_checker(password):
    if len(password) < 8:
        return "Weak password: password should be at least 8 characters long!"
    else:
        return "Strong password"

entered_password = input("Enter your password: ")
print(password_strength_checker(entered_password))



# 9) Creating a function that takes a text as input and returns the count of vowels (a, e, i, o, u) in the string.

def vowel_counter(text):
    vowel_count = 0
    for letter in text:
        if letter == "a":
            vowel_count += 1
        elif letter == "e":
            vowel_count += 1
        elif letter == "i":
            vowel_count += 1
        elif letter == "o":
            vowel_count += 1
        elif letter == "u":
            vowel_count += 1
    return vowel_count

entered_text = input("Enter a text: ")

print("Number of vowels in entered text:", vowel_counter(entered_text))



# 10) Writing a function that converts temperature from Celsius to Fahrenheit. Allowing the user to choose the conversion type.

def temperature_converter(temperature, unit):
    if conversion_type == "A":
        converted_temperature = (temperature * 9/5) + 32
        return temperature, "Celsius =", converted_temperature, "Fahrenheit"
    elif conversion_type == "B":
        converted_temperature = (temperature - 32) * 5/9
        return temperature, "Fahrenheit =", converted_temperature, "Celsius"
    else:
        return "Invalid choice"

temperature = float(input("Enter the temperature: "))
conversion_type = input("Enter A (to convert from C to F) or B (to convert from F to C): ")

print(temperature_converter(temperature, conversion_type))