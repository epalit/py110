"""
Write a function that finds the different number in a given list of numbers

Input: list of numbers
Output: int (the different one)

Rules:
- The list will always contain at least 3 numbers, and there will always be 
exactly one number that is different.

Algorithm:
- Build a dict of counts
- return the key with value 1
"""

def what_is_different(numbers):
    counts = {}

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    for number, count in counts.items():
        if count == 1:
            return number

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)