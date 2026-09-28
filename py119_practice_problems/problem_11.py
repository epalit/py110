"""
Write a function that finds the smallest substring of a given string that can
be multiplied to create the string

Input: string
Output: tuple (<substring>, <multiplier>)

Rules:
- find the smallest substring and largest multiplier
- assume the input is all lowercase alphabetic characters

Algorithm:
- iterate over a range from 1 to length of string + 1
    - each iteration check if len of string is divisible by the string slice len
        - if yes, multiply by the result and if you get the input string, 
        return the tuple
"""

def repeated_substring(string):
    for end_idx in range(1, len(string) + 1):
        if len(string) % (end_idx) == 0:
            multiplier = len(string) // (end_idx)
            substring = string[0:end_idx]

            if multiplier * substring == string:
                return (substring, multiplier)


print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))