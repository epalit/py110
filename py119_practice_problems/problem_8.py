"""
Write a function that calculates the length of the longest vowel substring of
a given string

Input: string
Output: int

Rules:
- string will always be lowercase

Algorithm:
- iterate over the word
    - if the letter is not a vowel
        - if vowel_count is bigger than max, store it as max
        - reset count to 0
    - if it is
        - add one to count
- if vowel_count is bigger than max, store it as max
- return max
"""
VOWELS = 'aeiou'

def longest_vowel_substring(string):
    count = 0
    max_count = 0
    for char in string:
        if char in VOWELS:
            count += 1
        else:
            max_count = count if count > max_count else max_count
            count = 0
    max_count = count if count > max_count else max_count

    return max_count

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
print(longest_vowel_substring("palalangamalaleeMoo"))
