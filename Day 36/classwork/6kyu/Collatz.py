"""
Create a function collatz that returns a collatz sequence string starting with the positive integer argument passed into the function, in the following form:

"X0->X1->...->XN"

Where Xi is each iteration of the sequence and N is the length of the sequence.

Input: 4
Output: "4->2->1"

Input: 3
Output: "3->10->5->16->8->4->2->1"
"""

def collatz(n):
    result = [str(n)]
    n2 = n
    while n2 != 1:
        if n2 % 2 == 0:
            n2 = n2 // 2
        else:
            n2 = 3 * n2 + 1
        result.append(str(n2))
    return '->'.join(result)