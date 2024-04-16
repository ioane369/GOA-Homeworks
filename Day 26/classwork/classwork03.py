# Creating a function that takes the lengths of the legs of a right triangle as parameters and returns the length of the hypotenuse.

def hypotenuse_len_calculator(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c

print(hypotenuse_len_calculator(3, 4))