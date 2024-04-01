# Writing a function that takes a list of numbers as input and returns the sum of all the numbers that are greater than 10.

def num_filter_calculator(numbers):
    num_sum = 0

    for num in numbers:
        if num > 10:
            num_sum += num
    return num_sum

numbers_list = [3, 33, 10, 12]

print(num_filter_calculator(numbers_list))