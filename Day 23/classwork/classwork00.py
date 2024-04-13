# 1) Creating a function that counts even numbers in the given list

def even_number_counter(num_list):
    count = 0

    for num in num_list:
        if num % 2 == 0:
            count += 1

    return count

numbers = [1, 2, 3, 4, 5]
print(even_number_counter(numbers))


# 2) Creating a function that replaces even indexed elements in the given list or string with inputted replacement

def even_index_replacer(collection):
    replacement = input("Enter the replacement for even-indexed characters: ")

    if type(collection) == list:
        for index in range(len(collection)):
            if index % 2 == 0:
                collection[index] = replacement
        return collection
    
    elif type(collection) == str:
        new_collection = ""

        for index in range(len(collection)):
            if index % 2 == 0:
                new_collection += replacement
            else:
                new_collection += collection[index]
        return new_collection

list1 = ["a", 2, 4, "b", "d", 8]
print(even_index_replacer(list1))

string = "abcdefgh"
print(even_index_replacer(string))


# 3) Creating a function that finds the index of the last even number in the given list

def last_even_number(num_list):
    result = -1

    for index in range(len(num_list)):
        if num_list[index] % 2 == 0:
            result = index
            
    return result

list2 = [2, 4, 5, 6, 7, 8, 9, 11]
print(last_even_number(list2))