# Implementing a simple calculator that takes two numbers and an operator (+, -, *, /) as input from the user 
# and performs the corresponding operation. (Bonus task: adding ** operator)

num1 = float(input("Enter first number: "))
operator = input("choose operator (+, -, *, **, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif operator == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif operator == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif operator == "**":
    print(num1, "**", num2, "=", num1 ** num2)
elif operator == "/":
    if num2 == 0:
        print("Division by 0 can't be done")
    else:
        print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid operator")