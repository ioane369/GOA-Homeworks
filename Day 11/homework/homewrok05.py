# Writing a program that asks the user for their age and prints if user is child, teenager or adult (based on the entered age). 
# (using if-elif-else)

while True:
    age = int(input("Please enter your age: "))

    if age <= 12:
        print("You are a child")
    elif age > 12 and age <= 17:
        print("You are a teenager")
    else:
        print("You are an adult") 