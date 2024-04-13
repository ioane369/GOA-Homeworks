'''
You are given a list of numbers in the function, 
your task is to concatenate the even numbers in this list with "+" and return a string as the final result.  

example:
Input data: [1,2,3,4]
Final result: "2+4"

Note: 
if there is only one even number in the list, return it directly
and if there are no even numbers in the list, return an empty string.   

Without using join() !  '''

def conceterating_even_numbers(numbers_list):
    count = 0
    even_numbers = ""

    for num in numbers_list:
        if num % 2 == 0:
            count += 1
            even_numbers += str(num) + ","

    if count == 0:
        return ""
    
    elif count == 1: 
        return even_numbers[: -1]
    
    else:
        result = even_numbers.replace(",", "+")
        return result[: -1]
    
print(conceterating_even_numbers([1, 2, 3, 4, 5, 6]))
print(conceterating_even_numbers([0, 3, 5]))
print(conceterating_even_numbers([3]))