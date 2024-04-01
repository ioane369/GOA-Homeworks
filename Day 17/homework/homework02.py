# Writing a function that takes a list of numbers as input and returns a new list containing only the even numbers from the original list.

def even_numbers(numbers):
    filtered_nums = []

    for num in numbers:
        if num % 2 == 0:
            filtered_nums.append(num)
    return filtered_nums

numbers_list = [1, 3, 4, 6, 11, 16]

print(even_numbers(numbers_list))