"""
Write a function that finds the character that appears most often in a given string

Input: string
Output: single character string

Rules:
- if more than one character appears with the greatest frequenct, return the first
- uppercase and lowercase are considered the same

Algorithm:
- get the unique chars in the lowered string
- iterate over them
    - count the appearances in the lowered string
    - if it is greater than the largest seen so far, store it
- return the stored char
"""

def most_common_char(string):
    counts = {}
    lowercase_string = string.lower()

    for char in lowercase_string:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    return_char = None
    max_count = 0

    for char in lowercase_string:
        if counts[char] > max_count:
            max_count = counts[char]
            return_char = char

    return return_char

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')