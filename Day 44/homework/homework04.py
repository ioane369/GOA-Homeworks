'''
Task: Write an algorithm to find the second largest element in a list of N values. How many comparisons does your algorithm do in the worst case? (Later, we will see an algorithm that will do this with about N comparisons.)
'''

def find_second_largest(lst):
    if len(lst) < 2:
        return "List must have at least two elements"
    
    largest = lst[0]
    second_largest = float('-inf')

    for index in range(1, len(lst)):
        if lst[index] > largest:
            second_largest = largest
            largest = lst[index]
        elif lst[index] > second_largest and lst[index] != largest:
            second_largest = lst[index]
    
    return second_largest

'''
1) For example, in the list [1, 4, 2, 3]:

For the element 4:
It's greater than 1, so 'second_largest becomes' 1 and 'largest' becomes 4. (1 comparison for the 'if' condition)

For the element 2:
It's not greater than 4, but it's greater than 1, and it's not equal to 4, so 'second_largest' becomes 2. (1 comparison for the 'if' condition, 2 comparisons for the 'elif' condition)

For the element 3:
It's not greater than 4, but it's greater than 1, and it's not equal to 4, so 'second_largest' becomes 3. (1 comparison for the 'if' condition, 2 comparisons for the 'elif' condition)

So, in this case, the total number of comparisons is 1 + 3 + 3 = 7.

So in cases like this, where second element is 'largest' and every subsequent element is candidate for 'second_largest', there will be done 1 comparison for second element (index 1), in 'if' statement and 3 comparison for every next element (1 comparison for the 'if' condition, 2 comparisons for the 'elif' condition)
'''