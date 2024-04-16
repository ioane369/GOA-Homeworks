'''
1) Creating a range-like function. Users must pass three arguments: start, end (inclusive), and step. 
The third argument (step) is optional; users are not required to pass it. In its absence, it will default to 1.   '''

def my_range(start, end, step = 1):
    numbers = []
    while start < end + 1:
        numbers.append(start)
        start += step
    return numbers

print(my_range(3, 10))

print(my_range(3, 10, 3))

# 2)  In the form of a comment, explaining the purpose of the keyword "return"

# The return keyword is used to exit a function and return a value back to the caller