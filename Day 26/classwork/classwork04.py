'''
Creating a function that takes a name as an argument. 
If the length of the name is greater than 5, the function returns its uppercase; otherwise, it returns the name capitalized.   '''

def modifying_name(name):
    if len(name) > 5:
        return name.upper()
    else:
        return name.capitalize()

# Test cases:

print(modifying_name("david"))   # Output should be "David"

print(modifying_name("orientadze"))   # Output should be "ORIENTADZE"