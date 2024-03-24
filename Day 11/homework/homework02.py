# writing a program that calculates the sum of all numbers entered by the user (using a while loop)
# after user enters all the numbers he/she has to enter 0 to calculate sum of those numbers

num_sum = 0

while True:
    num = int(input("Enter a number: "))
    
    if num == 0:
        break
    else:
        num_sum += num
print("Sum of entered numbers is", num_sum)