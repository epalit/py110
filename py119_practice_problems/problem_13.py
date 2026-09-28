"""
Write a function that determins whether some of the chars in a given string can
be rearranged to match the characters in another given string

Input: two strings
Output: bool

Rules:
- assume both args contains only lowercase letters
- assume neither string is empty

Algorithm:
- count occurences of letters in second arg and store as a dictionary
- iterate over the dict items
    - if the value for the key is greater than count of the key in arg 1, return false
- return True
"""

def unscramble(scrambled, word):
    counts = {}
    for char in word:
        counts[char] = counts.get(char, 0) + 1

    for letter, count in counts.items():
        if scrambled.count(letter) < count:
            return False

    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)