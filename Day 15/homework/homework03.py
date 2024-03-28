# Asking the user for five names (using input five times). Adding all of them into one list and printing only the first three names.

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
name3 = input("Enter third name: ")
name4 = input("Enter fourth name: ")
name5 = input("Enter fifth name: ")

names = [name1, name2, name3, name4, name5]

print("The first three names in the list are: ", names[: 3])