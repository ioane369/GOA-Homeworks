'''
Manual Sum Function: 
Create a function called manual_sum that iterates over list and adds their sum in a variable, then returns variable. 
Use for loop for this task. 
'''
def manual_sum(numbers_list):
    sum = 0
    
    for num in numbers_list:
        sum += num
    return sum

# Test cases:

print(manual_sum([1, 2, 3, 4]))   # Output should be 10
print(manual_sum([10, 20, 30]))   # Output should be 60
print(manual_sum([5, 4, 3, 2]))   # Output should be 14