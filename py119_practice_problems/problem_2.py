"""
Write a function that calculates the minimum sum of 5 consecutive numbers in a 
list

Input: list of ints
Output: int representing the sum, or None if the list has 4 or less elements

Rules:
- integers can be negative

Algorithm:
- return None if list length is 4 or less
- calculate the sums of all slices of 5 consecutive numbers
  - start idx to 0
  - end idx to 5
  - sums to []
  - while end idx < length of the list
    - sum list slice from start to end idx
    - append sum to sums list
    - increment indicies by 1
- return the minimum of those sums
"""

def minimum_sum(numbers):
    if len(numbers) <= 4:
        return None

    start_idx = 0
    end_idx = 5
    sums = []

    while end_idx < len(numbers) + 1:
        sums.append(sum(numbers[start_idx:end_idx]))
        start_idx += 1
        end_idx += 1

    return min(sums)

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)