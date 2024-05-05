"""
Create a function called manual_replace that takes a list, an element to replace, and the replacement element. The function should return a new list in which all instances of the specified element are replaced with the replacement element.
Do not use built-in functions to perform this task; you must implement your own logic.
"""

def manual_replace(lst, element_to_replace, replacement):
    modified_lst = []
    for element in lst:
        if element == element_to_replace:
            modified_lst.append(replacement)
        else:
            modified_lst.append(element)
    return modified_lst

# Test case:
num_lst = [10, 11, 10, 11]
print(manual_replace(num_lst, 10, 20))