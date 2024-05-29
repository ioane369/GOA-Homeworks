'''
Task: There is a set of numbers stored in a file, but we don't know how many it contains. Write an algorithm in pseudocode to calculate the average of the numbers stored in this file. What type of operations does your algorithm do? How many of each of these operations does your algorithm do?
'''

def calculate_average(numbers):
    if not numbers:
        return 0
    
    num_count = 0
    num_sum = 0

    for num in numbers:
        num_count += 1
        num_sum += num
        
    return num_sum / num_count

'''
1) My algorithm performs comparison, incrementation, addition, division and return operations.
2) It includes 1 comparison (for checking if the list is empty), N incrementations (for incrementing num_count), N additions (for adding numbers to num_sum), 1 division (for dividing 'num_sum' by 'num_count' to calculate the average), and 1 return (for returning the calculated average).

Note: N represents the number of elements in the list of numbers passed to the 'average_calculator' function
'''