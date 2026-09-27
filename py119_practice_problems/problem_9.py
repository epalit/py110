"""
Write a function that calculates the number of times a string occurs in another
string

Input: two strings
Output: int

Rules:
- overlapping strings don't count
- second argument won't be an empty string

Algorithm:
"""

def count_substrings(string, substring):
    count = 0
    idx = 0
    length = len(substring)

    while idx <= len(string) - length:
        if string[idx:idx + length] == substring:
            count += 1
            idx += length
        else:
            idx += 1

    return count

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)