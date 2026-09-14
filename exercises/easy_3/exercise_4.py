"""
# Problem
input: string
output: string with consonants doubled

requirements:
- do not double vowels, digits, whitespace or punctuation
- only ASCII is included
"""

def is_consonant(char):
    return char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

def double_consonants(text):
    result = ""
    for char in text:
        if is_consonant(char):
            result += char * 2
        else:
            result += char
    return result

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")