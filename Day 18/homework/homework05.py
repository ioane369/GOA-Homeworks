# Creating a function that receives a word as a parameter, reverses that word, and returns it.

def reversed_word(word):
    reversed_word = word[: : -1]
    return reversed_word

print(reversed_word("Hello"))