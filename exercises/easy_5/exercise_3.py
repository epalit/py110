VOWELS = "aeiou"

def remove_vowels_from_word(word):
    result = ""
    for char in word:
        if char.lower() not in VOWELS:
            result += char
    return result

def remove_vowels(words):
    return [remove_vowels_from_word(word) for word in words]

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True