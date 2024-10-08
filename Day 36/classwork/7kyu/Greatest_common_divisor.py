"""
Find the greatest common divisor of two positive integers. The integers can be large, so you need to find a clever solution.

The inputs x and y are always greater or equal to 1, so the greatest common divisor will always be an integer that is also greater or equal to 1.
"""

def mygcd(x, y):
    for num in range(min(x, y), 0, -1):
        if x % num == 0 and y % num == 0:
            return num