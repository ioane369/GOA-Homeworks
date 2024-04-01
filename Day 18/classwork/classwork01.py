# The user enters the length and width of a rectangle. Creating a function that will return the area of the rectangle.

def calculating_rectangle_area(num1, num2):
    return num1 * num2

length = int(input("Enter length of a rectangle: "))
width = int(input("Enter width of a rectangle: "))

print(calculating_rectangle_area(length, width))