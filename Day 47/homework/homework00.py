# Task: We wrote a function to find the maximum for 4 elements; now, let's write one for 5 elements.

def find_maximum(num1, num2, num3, num4, num5):
    maximum = num1
    if maximum < num2:
        maximum = num2
    if maximum < num3:
        maximum = num3
    if maximum < num4:
        maximum = num4
    if maximum <num5:
        maximum = num5
    return maximum

print(find_maximum(1, 4, 6, 5, 1))