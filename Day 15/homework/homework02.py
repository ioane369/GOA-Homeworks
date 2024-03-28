# Writing an algorithm that takes a string as input and returns True if first character of that string is "G".

inputted_string = input("Enter a string: ")

def starts_with_G(inputted_string):
    if inputted_string[0] == "G":
        return True
    else:
        return False

print(starts_with_G(inputted_string))