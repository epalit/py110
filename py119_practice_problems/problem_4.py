"""
Write a function that finds the two closest together numbers in a list

Input: list of ints
Output: tuple of the two closest ints in the list

Rules:
- closest means smallest difference
- if multiple pairs have the smallest difference, choose the pair that appears first

Algorithm:
- set differences dictionary {}
- iterate over range 1 to list length
- for each iteration
    - create a tuple of the current idx and idx - 1
    - calculate the difference
    - if difference in dict, append tuple to list value otherwise add it to dict
- get the first tuple from the smallest key and return it
"""

# def closest_numbers(numbers):
#     differences = {}

#     for idx_first in range(len(numbers) - 1):
#         for idx_second in range(idx_first + 1, len(numbers)):
#             pair = (numbers[idx_first], numbers[idx_second])
#             difference = max(pair) - min(pair)
#             if difference in differences:
#                 differences[difference].extend([pair])
#             else:
#                 differences[difference] = [pair]

#     return differences[min(differences)][0]

def closest_numbers(numbers):
    smallest_difference = float('inf')
    pair = None

    for first_idx in range(len(numbers) - 1):
        for second_idx in range(first_idx + 1, len(numbers)):
            first_num = numbers[first_idx]
            second_num = numbers[second_idx]
            difference = abs(first_num - second_num)

            if difference < smallest_difference:
                pair = (first_num, second_num)
                smallest_difference = difference

    return pair


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))