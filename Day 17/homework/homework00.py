# Writing a function that takes a list of numbers as input and returns the sum of all the numbers in the list.

def sum_of_numbers(numbers):
    num_sum = 0
    
    for num in numbers:
        num_sum += num
    return num_sum

numbers_list = [1, 2, 3, 4, 5]

print(sum_of_numbers(numbers_list))