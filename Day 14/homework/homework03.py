# Creating a list. Asking the user for their age, and if the age is over 18, asking for their name. 
# Then adding this name to the already created list and printing the updated list.

user_info = []
age = int(input("Enter your age: "))
user_info.append(age)

if age > 18:
    name = input("Enter your name: ")
    user_info.append(name)
    
print(user_info)