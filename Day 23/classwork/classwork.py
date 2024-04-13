#                                                        METHODS

#                                                replace()   (for strings)
'''
   The replace() method in Python is used to create a new string where all occurrences of a specified substring or character 
within the original string are replaced with another specified substring or character. 
It does not modify the original string; instead, it returns a new string with the replacements made.   '''

username = "Ioane Dolidze"
print(username.replace("o", "3"))

# How it works:

def my_replace(word, char_to_replace, replacement):
    changed_word = ''

    for char in word:
        if char == char_to_replace:
            changed_word += replacement
        else:
            changed_word += char
    
    return changed_word

print(my_replace("book", "o", "3"))


#                                              count()   (for strings and lists)
'''
   The count() method in Python is used to count the number of occurrences of a specified element within a sequence, 
such as a string or a list. It returns the count of how many times the specified element appears in the sequence.   '''

word = "Ioane"
print(word.count("o"))

list1 = (1, 1, 2, 3, 1, 4)
print(list1.count(1))

# How it works:

def my_count(collection, element_to_count):
    count = 0

    for element in collection:
        if element == element_to_count:
            count += 1
    
    return count

print(my_count("banana", "n"))
print(my_count([2, 3, 4, 2, 2, 2], 2))


#                                                    find()   (for strings)
'''
   The find() method in Python is used to search for a substring within a string and returns the lowest index in the string 
where the substring is found. If the substring is not found, it returns -1.   '''

string = "apple"
print(string.find("p"))

# How it works:

def my_find(string, char_to_find):
    for index in range(len(string)):
        if string[index] == char_to_find:
            return index
    return -1

print(my_find("elephant", "e"))