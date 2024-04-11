#                                              upper() and lower()

# The functions upper() and lower() allow you to quickly change the case of a string to all in uppercase or lowercase, respectively.
# Functions that only work on certain objects (strings, lists, etc.) are called using dot notation.

print('SmArTpHoNe'.lower())
print('SmArTpHoNe'.upper())

#                                                capitalize()

# The capitalize() function converts the first character of a string to uppercase, while making the remaining characters lowercase.

print("happy birthday".capitalize())

#                                                  find()
''' 
The find() function checks if a character (or a pattern of characters) is present in a string. 
The function returns the index (position) of the given value. 
If the given value is present multiple times, the function will return the first occurrence (the lowest index).   '''

print("Bee".find("e"))

# find() will return -1 if the value can't be found in the string.

print("robot".find("A"))