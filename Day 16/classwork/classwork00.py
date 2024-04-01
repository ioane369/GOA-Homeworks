# Creating a function that prompts the user for a number and prints a number 3 times that number

def multiplied_num(num):     # (num) არის პარამეტრი (როცა ფუნქციას ვქმნით)
    num = int(input("Enter a number: "))
    print(num * 3)


# Calling that function 5 times on different numbers to test it

multiplied_num(1)     # (1) არის არგუმენტი (როცა ფუნქციას ვიძახებთ)
multiplied_num(2)
multiplied_num(3)
multiplied_num(4)
multiplied_num(5)