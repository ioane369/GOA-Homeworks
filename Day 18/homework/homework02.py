"""Asking the user for the starting and ending numbers.
Passing these numbers to the function, storing the numbers between them in the list (using a for loop).
Then filtering (again with a for loop) - if the number is even,
adding that number raised to the second power to the new list, and if the number is odd, adding its square root.   """

start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))

def num_filter(num1, num2):
    numbers = []
    for num in range(start, end +1):
        numbers.append(num)
    filtered_list = []
    for num in numbers:
        if num % 2 == 0:
            filtered_list.append(num * num)
        else:
            filtered_list.append(num ** 0.5)
    return filtered_list

print(num_filter(start, end))