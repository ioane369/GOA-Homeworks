'''
Task: Write an algorithm that takes in three distinct integers and determines the largest of the three. What are the possible input classes that would have to be considered when analyzing this algorithm? Which one causes your algorithm to do the most comparisons? Which one causes the least? (If there is no difference between the most and least, rewrite the algorithm with simple conditionals and without using temporary variables so that the best case gets done faster than the worst case.)
'''

def find_largest(int1, int2, int3):
    if int1 > int2 and int1 > int3:
        return int1
    elif int2 > int1 and int2 > int3:
        return int2
    else:
        return int3

'''
1) When analyzing this algorithm, the possible input classes to consider are: int1 is the largest; int2 is the largest; int3 is the largest.
2) Most comparisons are done when int3 is the largest.
3) Least comparisons are done when int1 is the largest.
'''