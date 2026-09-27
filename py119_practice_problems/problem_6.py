"""
Write a function that counts the lowercase letters in a string and returns them

Input: string
Output: dict of the counts of lowercase letters in the string

Algorithm:
1. iterate over string
2. if the char is a lowercase letter add it to the dict or increment the count
3. return the dict
"""

def count_letters(string):
    counts = {}

    for char in string:
        if char.islower():
            counts[char] = counts.get(char, 0) + 1

    return counts

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})

