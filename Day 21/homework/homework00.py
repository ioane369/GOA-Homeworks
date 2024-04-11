#                                          WORKING IN CODEWARS

# 1) Beginner - Reduce but Grow

#Given a non-empty array of integers, return the result of multiplying the values together in order. 
#Example: [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    product = 1
    for num in arr:
        product *= num
    return product



# 2) Calculate BMI
'''
Write function bmi that calculates body mass index (bmi = weight / height2).
if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese"  '''

def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"
    


# 3) Vowel Count
'''
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.   '''

def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count


# 4) Square Every Digit
'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
Note: The function accepts an integer and returns an integer.   '''

def square_digits(num):
    result = ""
    for digit in str(num):
        digit = int(digit) ** 2
        result += str(digit)    
    return int(result)



# 5) Descending Order
'''  
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321   '''

def descending_order(num):
    digits = [int(digit) for digit in str(num)]
    result = ""
    
    for digit in str(num):
        max_digit = max(digits)
        result += str(max_digit)
        digits.remove(max_digit)
    return int(result)

# Another way

def descending_order(num):
    result = ""
    new_list = list(str(num))
    new_list.sort(reverse = True)
    for char in new_list:
        result += char 
    return int(result)



# 6) Who likes it?
'''
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item. 

It must return the display text as shown in the examples:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.  '''

def likes(names):
    if len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:            
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif len(names) > 3:
        return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
    else:
        return "no one likes this"
    


# 7) Multiples of 3 or 5
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.   '''

def solution(number):
    sum = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum