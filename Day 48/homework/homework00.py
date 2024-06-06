# Redo the katas from the classwork folder and explain each one using comments.

# 1) Even or Odd

def even_or_odd(number):    # This function takes a number as an argument and returns "Even" if the number is even and "Odd" if it is odd.
    if number % 2 == 0:    # Checking if the remainder is 0 when the number is divided by 2)
        return "Even"    # If the number is divisible by 2 (without remainder), returning the string "Even".
    return "Odd"    # If the number is not divisible by 2 (without remainder), returning the string "Odd".



# 2) Reversed Strings

def solution(string):    # This function takes a string as an argument and returns the reversed string.
    return string [::-1]    # Reversing the string using slicing. The [::-1]slice notation means start at the end of the string and end at position 0, move with the step -1



# 3) String repeat

def repeat_str(repeat, string):    #  This function takes an integer "repeat" and a string "string" as arguments and returns "string" repeated "repeat" number of times.
    return string * repeat    # Multiplying "string" by the integer "repeat" to get the string repeated "repeat" times.



# 4) Sum of two lowest positive integers

def sum_two_smallest_numbers(numbers):    # This function takes a list of numbers as an argument and returns the sum of the two smallest numbers in the list.
    numbers.sort()    # Sorting the list of numbers in ascending order.
    return numbers[0] + numbers[1]     # Returning the sum of the first two elements in the sorted list, which are the two smallest numbers.   



# 5) Maximum Multiple

def max_multiple(divisor, bound):    # This function takes two arguments: "divisor" and "bound", and returns the largest number less than or equal to "bound" that is divisible by "divisor".
    for num in range(bound, divisor - 1, -1):    # Iterating from "bound" down to "divisor" in steps of -1. (The range is inclusive of "bound" and "divisor").
        if num % divisor == 0:    # Checking if current number is divisible by "divisor" without remainder.
            return num    # If current number is divisible by "divisor", returning it.
        


# 6) JavaScript Array Filter
        
def is_even(num):    # This function checks if a given number is even.
    return num % 2 == 0    # Returns True if "num" is divisible by 2 without remainder, otherwise returns False.
        
def get_even_numbers(arr):    # This function takes a list "arr" of numbers as input and returns a new list containing only the even numbers from "arr".
    return list(filter(is_even, arr))    # Using the filter function with "is_even" as the filtering function to select only those elements from "arr" for which "is_even" returns True, then Converting the filtered result into a list and returning it.



# 7) Check the exam

def check_exam(arr1,arr2):    # This function compares the student's answers (arr2) with the correct answers (arr1) and calculates the score based on the comparison.
    score = 0    # Declaring the score variable to keep track of the student's score.
    for index in range(len(arr2)):    # Iterating through each index of arr2.
        if arr2[index] == "":    # Cheacking if answer is empty.
            pass    # Skipping empty answers (because empty answer equals 0 score).
        elif arr2[index] == arr1[index]:    # Checking if answer is correct.
            score += 4    # Increasing "score" by 4 point for every correct answer.
        else:
            score -= 1    # Decreasing "score" by 1 point for every incorrect answer.
    if score < 0:    # Checking if "score" is negative.
        return 0    # Returning 0 if "score" is negative.
    return score    # Returning the calculate score if it's not negative.



# 8) Row Weights

def row_weights(array):    # This function calculates the total weight of two groups based on the array of weights given. The even-indexed elements are considered the weights of team 1, and the odd-indexed elements are considered the weights of team 2.
    return sum(array[::2]), sum(array[1::2])    # Firstly, calculating the sum of weights for team 1 (even-indexed elements) using slicing. "array[::2]:" slices the array starting from the first element (0 index) and selects every second element. So, "array[::2]" gives us all elements at even indices.
    # Then Calculating the sum of weights for team 2 (odd-indexed elements) using slicing. array "[1::2]:" slices the array starting from the second element (1 index) and selects every second element. So, "array[1::2]" gives us all elements at odd indices.
    # Lastly, returning the sum of weights for team 1 and team 2.