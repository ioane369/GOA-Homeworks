# Creating a function that takes a list of numbers as a parameter and returns the arithmetic mean for that list.

def calculating_arithmetic_mean(numbers):
    num_sum = 0
    arithmetic_mean = 0
    for num in numbers:
        num_sum += num
    arithmetic_mean = num_sum / len(numbers)
    return arithmetic_mean

numbers = [3, 6, 33, 14, 8]

print(calculating_arithmetic_mean(numbers))