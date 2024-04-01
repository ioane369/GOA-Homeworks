# Writing a function that takes a list of numbers as input and returns a new list containing the square of each number.

def squared_numbers(numbers):
    squared_numbers = []

    for num in numbers:
        squared_numbers.append(num * num)
    return squared_numbers

numbers_list = [1, 2, 3, 4, 5]

print(squared_numbers(numbers_list))