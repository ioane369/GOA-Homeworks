'''
Copy function of reduce: 
Define a function named manual_reduce that takes a list as input, then create an empty list named copied_list to store the copied items inside it. 
Then use for loop to loop over each item in the original list, append them to the copied_list. 
In the end, return the copied_list after iterating through all items.
finally demonstrate the usage of the manual_reduce function by creating an original list, making a copy of it, 
and printing both the original and copied lists.
'''
def manual_reduce(list):
    copied_list = []
    for item in list:
        copied_list.append(item)
    return copied_list


original_list = [3, 2, 3, 2, 3, 2, 3, 2]
copied_list = manual_reduce(original_list)

print(original_list)
print(copied_list)