# Writing a function that takes a list of strings as input and returns a new list containing the lengths of each string.

def length_measurer(strings):
    length_list = []

    for string in strings:
        length_list.append(len(string))
    return length_list

string_list  = ["grandma", "rat", "tonka", "city"]

print(length_measurer(string_list))