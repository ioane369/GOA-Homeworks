# Writing a function that takes a list of strings as input and returns a new list 
# containing only the strings that have a length greater than 5.

def string_length_filter(strings):
    filtered_list = [] 

    for string in strings:
        if len(string) > 5:
            filtered_list.append(string)
    return filtered_list
        
string_list = ["apple", "banana", "car", "dog"]

print(string_length_filter(string_list))