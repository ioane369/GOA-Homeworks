'''
Task: Write an algorithm in pseudocode to count the number of capital letters in a file of text. How many comparisons does it do? What is the fewest number of increments it might do? What is the largest number? (Use N for the number of characters in the file when writing your answer.)
'''

def count_capiatal_letters(text):
    count = 0
    exceptions = [',', '.', '!', '?', ' ']

    for element in text:
        if element not in exceptions and element == element.upper():
            count += 1
            
    return count

'''
1) It performs 2N comparisons.
2) The fewest number of increments is 0.
3) The largest number of increments is N.
'''