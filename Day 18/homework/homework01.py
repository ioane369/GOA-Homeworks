# Creating a function that takes the name and the surname as a parameter, adds them to a list, and then returns the list.

def user_info(name, surname):
    user_info = []
    user_info.append(name)
    user_info.append(surname)
    return user_info

name = input("Enter your name: ")
surname = input("Enter your surname: ")

print(user_info(name, surname))