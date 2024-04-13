# Modifying this code so that the output does not start with a +

def my_join0(join_str, strings_list):
    joined_elements = ''

    for word in strings_list:
        joined_elements += join_str + word

    return joined_elements

list1 = ["1", "2", "3"]
print(my_join0("+", list1))

# Modified code:

def my_join1(join_str, strings_list):
    joined_elements = ''

    for word in strings_list:
        joined_elements += join_str + word

    return joined_elements[1:]

print(my_join1("+", list1))