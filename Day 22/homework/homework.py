#                                             WORKING IN CODEWARS 

#                                                   8 kyu

# 1) Sum of positive
'''
You get an array of numbers, return the sum of all of the positives ones.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0.   '''

def positive_sum(arr):
    sum = 0
    for num in arr:
        if num > 0:
            sum += num
    return sum


# 2) String repeat
'''
Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"   '''

def repeat_str(repeat, string):
    result = ""
    for i in range(repeat):
        result += string
    return result


# 3) Remove First and Last Character
'''
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
You're given one parameter, the original string. You don't have to worry about strings with less than two characters.   '''

def remove_char(s):
    s = list(s)
    s.pop(0) and s.pop(-1)
    return ''.join(s)


# 4) Square(n) Sum
'''
Complete the square sum function so that it squares each number passed into it and then sums the results together.
For example, for [1, 2, 2] it should return 9  '''

def square_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num** 2
    return sum


# 5) Grasshopper - Summation
'''
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.
For example (Input -> Output):
2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8) '''

def summation(num):
    summation = 0
    for i in range(1, num +1):
        summation += i
    return summation



#                                                     7 kyu

# 1) Disemvowel Trolls
'''
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.'''

def disemvowel(string):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for char in string:
        if char.lower() not in vowels:
            result += char
    return result


# 2) Highest and Lowest

# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.  

def high_and_low(numbers):
    new_list = numbers.split()
    result = []
    for i in new_list:
        result.append(int(i))
    return str(max(result)) + " " + str(min(result))


# 3) List Filtering
'''
create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
Example:
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]   '''

def filter_list(l):
    new_list = []
    for char in l:
        if type(char) == int:
            new_list.append(char)
    return new_list


# 4) You're a square!
'''
Given an integral number, determine if it's a square number:
Examples:
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false   '''

def is_square(n):
    square_root = n ** 0.5
    return square_root * square_root == n


# 5) Get the Middle Character
'''
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"   '''

def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        return s[(length // 2) - 1: (length // 2) + 1]
    else:
        return s[length // 2]