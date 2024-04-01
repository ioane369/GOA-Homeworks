# creating a function that will filter the passed numbers (in this case from 1 to 20) and return only multiples of 4.

def num_filter(numbers):
    return numbers[3: : 4]

num_list = list(range(1, 20 + 1))

print(num_filter(num_list))