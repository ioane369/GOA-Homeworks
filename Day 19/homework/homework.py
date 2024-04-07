#                                         WORKING IN CODEWARS

# 1) Find the smallest integer in the array

# Given an array of integers your solution should find the smallest integer.

def find_smallest_int(arr):
    smallest = arr[0]
    
    for num in arr:
        if smallest > num:
            smallest = num
    return smallest



# 2) Remove String Spaces

# Write a function that removes the spaces from the string, then return the resultant string.

def no_space(x):
    new_string = ""

    for char in x:
        if char != ' ':
            new_string += char
    return new_string



# 3) Convert a Boolean to a String

# Implement a function which convert the given boolean value into its string representation.
# Note: Only valid inputs will be given.

def boolean_to_string(b):
    return str(b)
    


# 4) Sum Arrays
    
# Write a function that takes an array of numbers and returns the sum of the numbers. 
# The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
    
def sum_array(a):
    num_sum = 0

    for num in a:
        num_sum += num
    return num_sum



# 5) Abbreviate a Two Word Name

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this: Sam Harris => S.H

def abbrev_name(name):  
    index = -1 

    for i in range(len(name)):
        if name[i] == " ":
            index = i
    
    if index != -1:
        first_initial = name[0].upper()
        second_initial = name[index + 1].upper()
        result = first_initial + "." + second_initial
    return result



# easier way:

def abbrev_name(name):
    name = name.upper()

    split_name = name.split()
    first_initial = split_name[0]
    second_initial = split_name[1]
    return first_initial[0] + "." + second_initial[0]



# 6) Beginner - Lost Without a Map

# Given an array of integers, return a new array with each value doubled.

def maps(a):
    doubled_numbers = []

    for num in a:
        doubled_numbers.append(num * 2)
    return doubled_numbers



# 7) MakeUpperCase

# Write a function which converts the input string to uppercase.

def make_upper_case(s):
    return s.upper()



# 8) Calculate average

# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    sum = 0
    result = 0
    for num in numbers:
        sum += num
    result = sum / len(numbers)
    return result



""" 9) Calculate BMI
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"   """

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