# printing the sum of the first ten numbers (using for loop)

num  = 1
num_sum = 0
for i in range(10):
    print(num)
    num_sum = num_sum + num
    num = num + 1
print(num_sum)