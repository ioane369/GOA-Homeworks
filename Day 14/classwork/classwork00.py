# Creating a list of my favourite movies and TV series, then printing it.

movies_TVseries = ["Fight Club", "12 Angry Men", "Se7en", "Breaking Bad",]
print(movies_TVseries)


# Printing a single value from the list using indexing

print(movies_TVseries[1])


# Declaring a variable named "fav" and assigning its value from the list using indexing.

fav = movies_TVseries[0]
print(fav)


# Printing the last two elements in the list using negative indexing.

print(movies_TVseries[-1], movies_TVseries[-2])


# Asking the user for their favourite car and then declaring a variable named "fav_car",
# followed by creating a list called "cars", containing the variable "fav_car" and printing it.

fav_car = input("Enter your favourite car: ")
cars = ["Ford", "Audi", fav_car]

print(cars)