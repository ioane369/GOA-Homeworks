"""
Create a function called manual_count that takes a collection and a value to count. The function should return the number of times the specified value appears in the collection.
Do not use built-in functions to perform this task; you must implement your own logic.
"""

def manual_count(collection, value_to_count):
    count = 0
    for value in collection:
        if value == value_to_count:
            count += 1
    return count

# Test case:
num_lst = [12, 13, 14, 12, 14, 100]
print(manual_count(num_lst, 12))