# Write a program that outputs the minimum and maximum values of five types: signed char, short int, int, long int, and long long int.

types_and_bits = {
    'signed_char': 8,
    'short int': 16,
    'int': 32,
    'long int': 64,
    'long long int': 64, 
}

def min_max_values(type):
    # Formula for minimum value: -2^(n-1), where n represents the number of bits.
    min_value = -2 ** (types_and_bits[type] - 1)
    # Formula for maximum value: 2^(n-1) - 1, where n represents the number of bits.
    max_value = 2 ** (types_and_bits[type] - 1) - 1
    return f'{type} \nMinimum value: {min_value} \nMaximum value: {max_value}'

print(min_max_values('signed_char'))
print(min_max_values('short int'))
print(min_max_values('int'))
print(min_max_values('long int'))
print(min_max_values('long long int'))