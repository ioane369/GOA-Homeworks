"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    result = []
    exceptions = [",", ".", "!", "?"]
    for element in text.split():
        if element in exceptions:
            result.append(element)
        else:
            word_to_add = element[1: ] + element[0] + "ay"
            result.append(word_to_add)
    return " ".join(result)