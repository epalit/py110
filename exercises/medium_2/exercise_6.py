"""
Write a function that calculates the difference between:
- sum(positive integers up to and including the provided number) ** 2
- sum(each positive integer ** 2)

Input: int (assume positive)
Output: int calculated as above

Algorithm:
1. Generate the positive integers up to and including the provided number
2. calculate sum(integers) ** 2
3. calculate sum(each integer ** 2)
4. return (2) - (3)
"""

def sum_square_difference(number):
    integers = range(1, number + 1)

    square_of_sum = sum(integers) ** 2
    sum_of_squares = sum(num ** 2 for num in integers)

    return square_of_sum - sum_of_squares

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True
