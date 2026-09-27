"""
Write a function that counts the number of identical pairs of ints in a list

Input: list of ints
Output: int (count of pairs)

Rules:
- lists length 1 or less return 0
- If a certain number occurs more than twice, count each complete pair once

Algorithm:
- iterate over list
    - build dictionary of counts
- for each element in dictionary
    - add count values // 2 to total
- return total
"""

def pairs(numbers):
    counts = {}

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    total = 0
    for count in counts.values():
        total += count // 2

    return total

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
