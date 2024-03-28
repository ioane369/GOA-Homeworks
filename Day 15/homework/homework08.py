# Asking the user for a number. Then, creating a list that will contain even numbers from 0 to the user's number (using a for loop). 
# Finally, printing the entire list.

finish = int(input("Enter a number: "))

even_numbers = []

for num in range(0, finish + 1, 2):
    even_numbers.append(num)

print("Even numbers from 0 to", finish, "are:", even_numbers)