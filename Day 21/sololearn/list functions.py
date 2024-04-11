#                                             len()
# len() stands for length and, when used on lists, it returns the number of items in the list.

movies = ["Avatar", "Titanic", "Avengers"]
print(len(movies))

# len() returns the number of items in a sequence

word = "apple"
print(len(word))

#                                            append()

# The append() function adds a new item to the end of a list. 

songs = ["Yesterday", "Hello", "Believer"]
songs.append("Imagine")
print(songs)

#                                            insert()

# The insert() function allows you to add an element to a list, at a specific position.
# insert() takes 2 arguments. The first is the index (where to insert) and the second is the item (what to insert).

items = ["book", "pen", "pencil"]
items.insert(2,"marker")
print(items)

#                                             pop()

# The pop() function removes an element from a list.
# That position indicated by the index is the only argument that the pop() function accepts.

letters = ["a", "b", "c"]
letters.pop(1)
print(letters)