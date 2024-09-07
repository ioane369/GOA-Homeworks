# Write a program that keeps track of the lengths of the entered strings. When given a specific input, it should return the longest string.

def longest():
    longest_sentence = ''

    while True:
        sentence = input('Enter a sentence: ')
        if sentence == 'stop':
            return longest_sentence
        if len(sentence) > len(longest_sentence):
            longest_sentence = sentence

print(longest())