'''
Creating a function called "filter" that takes two parameters: a collection as the first parameter and a value as the second. 
The function should return a new collection that does not contain the values passed as the second parameter.   '''

def filter(collection, element_to_remove):
    if type(collection) == list:
        new_collection = [] 
        for element in collection:
            if element != element_to_remove:
                new_collection.append(element)
        return new_collection
    elif type(collection) == str:
        new_collection = ""
        for element in collection:
            if element != element_to_remove:
                new_collection += element
        return new_collection
    else:
        return "Wrong collection"

# Test cases:
    
print(filter("abcddd", "d"))   # Output should be "abc"

print(filter([1, 2, 3, 4, 3, 3, 2, 3], 3))   # Output should be [1, 2, 4, 2]