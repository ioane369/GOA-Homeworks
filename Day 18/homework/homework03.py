"""Creating a function that takes the surname as a parameter. 
The function should move each letter of the last name to a new list. 
Then, by iterating through this list using a for loop, adding only the letters at even indexes to another list. 
Finally, returning this list. 
Bonus: converting this list to a string and returning it.   """

def modifying_surname(surname):
    surname_letters = []

    for letter in surname:
        surname_letters.append(letter)

    even_indexed_letters = []

    for index in range(len(surname_letters)):
        if index % 2 == 0:
            even_indexed_letters.append(surname_letters[index])

    return ''.join(even_indexed_letters)


user_surname = input("Enter your surname: ")

print(modifying_surname(user_surname))