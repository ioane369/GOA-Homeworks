# Discussing the code:

# This function searchs through given list of numbers and returns the last even number in that list.  

def find_last_even(numbers_list):   
# 1) Creating a function named "find_last_even", that takes only one parameter - "numbers_list", which is list of numbers that it should search through

    for i in range(len(numbers_list) - 1, -1, -1):
# 2) It iterates through the list in reversed order, for that it creates sequence of indexes in the range of given list's length.
# Sequence starts from last index and continues until -1 (including 0), on every iteration index decrements by 1.
    
        if numbers_list[i] % 2 == 0:
# 3) Inside the loop, it checks if the number at the current index is even. 
#(If a number is divisible by 2 without a remainder, the number is even)                

            return numbers_list[i]   
# 4) If an even number is found, function immediately returns it, breaks out of loop and ends function execution
# If there is no even number in the list, function returns "None".

# Testing if previously created function works correctly. If it does, it should print 4. 
print(find_last_even([1,2,3,4,5]))   