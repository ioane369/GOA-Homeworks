# writing every possible two-input functions, using comparison operations

#                                            "or" logical operation
 
print(5 > 3 or 5 < 3)   # result: True
print(5 < 3 or 5 > 3)   # result: True
print(5 > 3 or 5 > 4)   # result: True
print(5 < 3 or 5 < 4)   # result: False


#                                           "and" logical operation

print(3 > 2 and 3 < 2)   # result: False
print(3 < 2 and 3 > 2)   # result: False
print(3 > 2 and 3 > 1)   # result: True
print(3 < 2 and 3 < 1)   # result: False