"""
Write a function that counts the bumber of even substrings in a string of digits

Input: string
Output: int

Rules:
- If a substring occurs more than once, you should count each occurrence as
a separate substring

Algorithm:
- set count to 0
- iterate over the string with enumerate
    - if the int(digit) is even:
        - add the length of the slice up to that index to count
return count
"""

def even_substrings(string):
    count = 0

    for idx, digit in enumerate(string):
        if int(digit) % 2 == 0:
            count += idx + 1

    return count

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)
