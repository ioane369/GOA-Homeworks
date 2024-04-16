'''
Manual Min Function: 
Define a function named manual_min that iterates through list, updating a variable with the minimum value, then returns the minimum value found. 
Use for loop for this task.   
'''
def manual_min(numbers_list):
    minimum_value = numbers_list[0]

    for value in numbers_list:
        if value < minimum_value:
            minimum_value = value
    return minimum_value

# Test cases:

print(manual_min([1, 2, 3, 4]))   # Output should be 1
print(manual_min([10, 20, 30]))   # output should be 10
print(manual_min([5, 4, 3, 2]))   # output should be 2