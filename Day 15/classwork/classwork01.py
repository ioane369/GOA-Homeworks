""" 
Asking the user to enter a number. This number will serve as the starting point. 
Then, adding 10 to this number to determine the end point. Generating a list that includes every number 
from the starting point to the end point. Finally, printing every second element from this list. 
"""

start = int(input("Enter a number: "))
end = start + 10

num_list = []

for num in range(start, end + 1):
    num_list.append(num)

print(num_list[: : 2])
