# Creating a function that takes a list of numbers as a parameter and returns a filtered version of it that doesn't have duplicates.

def deduplication(numbers):
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

numbers = [11, 2, 11, 3, 78, 3]

print(deduplication(numbers))