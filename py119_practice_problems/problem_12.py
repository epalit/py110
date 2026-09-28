"""
Write a function that determines whether a string is a pangram

Input: string
Output: bool

Rules:
- a pangram is a string that contains every letter of the alphabet at least once
- case is irrelevant

Algorithm:
- create a set of the lowercase letters of the string
- if it is 26 length or more return True
- else False
"""

def is_pangram(string):
    lowercase_letters = set(char.lower() for char in string if char.isalpha())
    return len(lowercase_letters) >= 26

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)
