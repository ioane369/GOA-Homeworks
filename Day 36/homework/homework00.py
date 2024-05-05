"""
Create a function called manual_reverse that takes a sorted collection as an argument. The function should reverse the collection and return it in its reversed form.
Do not use built-in functions to perform this task; you must implement your own logic.
"""

def manual_reverse(collection):
    reversed_collection = []
    for index in range(len(collection) - 1, -1, -1):
        reversed_collection.append(collection[index])
    return reversed_collection

# Test case:
num_lst = [1, 2, 3, 4, 5]
print(manual_reverse(num_lst))