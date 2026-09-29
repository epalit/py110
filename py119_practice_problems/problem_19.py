"""
Write a function that finds the integer that occurs an odd number of times in a
given list

Input: list of ints
Output: int

Rules:
- There will always be exactly one such integer in the input list.

Algorithm:
- iterate over the list, building a dictionary of counts of ints
- iterate over the dict returning the key for the odd value
"""

def odd_fellow(numbers):
    counts = {}

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    for number, count in counts.items():
        if count % 2 == 1:
            return number

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)