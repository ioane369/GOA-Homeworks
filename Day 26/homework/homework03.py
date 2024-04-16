'''
Manual Len Function: 
Develop a function named manual_len that iterates through list, counting each element, and returns the count as the length of the list. 
Use for loop for this task.   
'''
def manual_len(list):
    count = 0

    for element in list:
        count += 1
    return count

# Test cases:

print(manual_len([3, 2, 3, 2, 3, 2, 3, 2]))   # Output should be 8
print(manual_len([10, 20, 30]))               # Output should be 3
print(manual_len([5, 4]))                     # Output should be 2