"""
Write a function that counts the number of disintict alphanumeric characters that
occur more than once in a given string

input: string
output: int

Rules:
- string only has alphanumeric chars
- distinct is case insensitive

Algorithm:
- set seen_chars = set(), counted_chars = set()
- iterate over string.lower()
    - each iteration if not in seen, add it
    - elif not in counted
- return length of counted_chars
"""

def distinct_multiples(string):
    seen_chars = set()
    counted_chars = set()

    for char in string.lower():
        if char not in seen_chars:
            seen_chars.add(char)
        elif char not in counted_chars:
            counted_chars.add(char)

    return len(counted_chars)

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5