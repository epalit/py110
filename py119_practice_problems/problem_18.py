"""
Write a function that calculates the index of the position in the list where
the sum of the numbers before is equal to the sum of all the numbers after

Input: list of integers
Output: int

Rules:
- if no index is found that satisfies the condition, return -1
- if there is more than one answer, return the smallest index
- the sum to the left of 0 is 0
- the sum to the right of the final position is 0

Algorithm
- iterate over a range of the length of the list
    - sum the slice before and after the current index
    - if the sums are equal return the index
return -1
"""

def equal_sum_index(numbers):
    for idx in range(len(numbers)):
        left_sum = sum(numbers[:idx])
        right_sum = sum(numbers[idx+1:])

        if left_sum == right_sum:
            return idx

    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)