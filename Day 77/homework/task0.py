# Write a program that converts a number to its decimal equivalent.

# Works only for bases less than 10
def convert_to_decimal(num, base):
    num = str(num)
    ln = len(num)
    res = 0

    for i in range(ln):
        res += int(num[i]) * (base ** (ln - (i + 1))) 
    return res

print(convert_to_decimal(110110, 2))
print(convert_to_decimal(753, 8))
print(convert_to_decimal(1435, 6))