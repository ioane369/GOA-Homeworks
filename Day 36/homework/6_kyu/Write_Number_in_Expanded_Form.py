"""
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
    st_num = str(num)
    rounded_num = ""
    step = 0
    for index in range(len(st_num)):
        if st_num[index] == "0":
            step += 1
            pass
        else:
            rounded_num += " + " + st_num[index]
            step += 1
            for digit in range(len(st_num) - step):
                rounded_num += "0"
    return rounded_num[3: ]