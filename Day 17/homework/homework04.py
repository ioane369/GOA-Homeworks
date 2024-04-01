# Writing a function that takes a list of strings as input and returns a new list containing only the strings that start with the letter 'a'.

def starts_with_a(strings):
    filtered_strings = []

    for string in strings:
        if string[0] == "a":
            filtered_strings.append(string)
    return filtered_strings

string_list = ["android", "hello", "day", "alone"]

print(starts_with_a(string_list))