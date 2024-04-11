# Optimizing this code:

def descending_order1(num):
    num_str = str(num)
    reversed_str = ""
    res_arr = []
    for i in range(len(num_str)-1, -1, -1):
        reversed_str += num_str[i]
    for i in reversed_str:
        res_arr.append(i)
    res_arr.sort(reverse = True)
    return int("".join(res_arr))

print(descending_order1(9823467))

# Optimized code:

def descending_order2(num):
    new_list = list(str(num))
    new_list.sort(reverse = True)
    return int(''.join(new_list))

print(descending_order2(9823467))