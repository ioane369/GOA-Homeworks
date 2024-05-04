"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
Notes:

the returned string should only contain lowercase letters
"""

def kebabize(st):
    new_str = ""
    result= ""
    for index in range(len(st)):
        if st[index].isnumeric():
            pass
        else:
            new_str += st[index]
            
    for index in range(len(new_str)):
        char = new_str[index]
        if index == 0:
            result += char.lower()
        elif char.isupper():
            result += "-" + char.lower()
        else:
            result += char
    return result