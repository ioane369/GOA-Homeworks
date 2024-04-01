""" Asking user how many numbers they want to enter, 
then creating a for loop where the user enters numbers as many times as they specified earlier
lastly creating function, that will calculate and return the sum of the entered numbers."""

num_quantity = int(input("How many numbers do you want to enter in list: "))

entered_nums = []

for i in range(num_quantity):
    num = int(input("Enter a number: "))
    entered_nums.append(num)


def sum_of_nums(entered_nums):
    num_sum = 0

    for num in entered_nums:
        num_sum += num
    return num_sum

print(sum_of_nums(entered_nums))


# creating a second function that will only return even numbers greater than 10.

def number_filter(entered_nums):
    filtered_numbers = []

    for num in entered_nums:
        if num > 10 and num % 2 == 0:
            filtered_numbers.append(num)
    return filtered_numbers

print("Even numbers greater than 10 in that list are:", number_filter(entered_nums))