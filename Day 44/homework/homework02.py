'''
Task: Write an algorithm, without using compound conditional expressions, that takes in three integers and determines if they are all distinct. On average, how many comparisons does your algorithm do? Remember to examine all input classes.
'''

def determine_distinct(int1, int2, int3):
    if int1 == int2:
        return 'Not all distinct'
    elif int1 == int3:
        return 'Not all distinct'
    elif int2 == int3:
        return 'Not all distinct'
    else:
        return 'All distinct'