"""
A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
(byte1)   (byte2)   (byte3)   (byte4)
should become:

10101010  00001111  00000000  11111111
(byte4)   (byte3)   (byte2)   (byte1)
The total number of bits will always be a multiple of 8.

The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
Note: In the C and NASM languages you are given the third parameter which is the number of segment blocks.
"""

def data_reverse(data):
    new_lst = []
    for index in range(len(data)):
        if (index + 1) % 8 == 0:
            new_lst.append(data[index])
            new_lst.append(3)
        else:
            new_lst.append(data[index])
    split_lsts = []
    current_lst = []
    for num in new_lst:
        if num == 3:
            split_lsts.append(current_lst)
            current_lst = []
        else:
            current_lst.append(num)
    split_lsts.reverse()
    result = []
    for sublist in split_lsts:
        for item in sublist:
            result.append(item)
    return result