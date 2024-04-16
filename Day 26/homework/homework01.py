'''
Manual Max Function: 
Define a function named manual_max that iterates through list, updating a variable with the maximum value, then returns the maximum value found. 
Use for loop for this task.   
'''
def manual_max(numbers_list):
    maximum_value = numbers_list[0]
    
    for value in numbers_list:
        if value > maximum_value:
            maximum_value = value
    return maximum_value

# Test cases:

print(manual_max([1, 2, 3, 4]))   # Output should be 4
print(manual_max([10, 20, 30]))   # output should be 30
print(manual_max([5, 4, 3, 2]))   # output should be 5