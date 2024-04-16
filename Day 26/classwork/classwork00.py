'''
Creating a list of numbers from 1 to 50, inclusive of 50. 
Then, creating a function that takes numbers list as input and returns the last number from the list that is a multiple of 4 and.
Finally, passing previously created list to this function and printing the result.  '''

list1 = []
for num in range(10, 51):
    list1.append(num)
 
def last_4_multiple(numbers_list):
    for index in range(len(numbers_list)-1, -1, -1):
        if numbers_list[index] % 4 == 0:
            return numbers_list[index]
        
print(last_4_multiple(list1))