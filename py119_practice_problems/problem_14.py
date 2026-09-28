"""
Write a function that calculates the sum of the multiples of 7 or 11 that are
less than the provided argument.

Input: int
Output: int (sum)

Rules:
- if a number is a multiple of 7 and 11, count it once
- if the argument is negative return 0

algorithm:
- if the argument is less than 0 return 0
- set multiple_sum to 0
- iterate over a range up to and not including the provided number
    - for each iteration if the number is divisible by 7, add it to the sum
    - elif divisible by 11, add it to the sum
- return multipl_sum
"""

def seven_eleven(limit):
    if limit < 0:
        return 0

    multiple_sum = 0

    for number in range(limit):
        if number % 7 == 0:
            multiple_sum += number
        elif number % 11 == 0:
            multiple_sum += number

    return multiple_sum


print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)