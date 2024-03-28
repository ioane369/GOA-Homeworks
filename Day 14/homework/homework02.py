""" Asking the user for two numbers and storing them as variables, both of type int. 
Then, using a for loop with the lower number as the start and the higher number as the end, 
printing only the multiples of five using an if statement."""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

start = min(num1, num2)
end = max(num1, num2)

multiples_of_5 = []

for num in range(start, end + 1):
    if num % 5 == 0:
        multiples_of_5.append(num)
        
print("Multiples of 5 from", start, "to", end, "are:", multiples_of_5) 