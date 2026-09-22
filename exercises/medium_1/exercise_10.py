"""
Write a function that returns the position in the Fibonacci series of the first
number that has the number of digits provided.

Input: int representing the number of digits
Output: int represeting the position of the first number with that num of digits

Rules:
- first Fibonacci number has an index of 1
- the argument will always be 2 or greater

Algorithm:
- set first previous to 1
- set second previous to 1
- set position to 2
- iterate over position until second prev digits >= length provided
- each iteration, set:
- second prev to first + second
- first prev to second
- position + 1
"""

import sys

sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(length):
    first_previous = 1
    second_previous = 1
    position = 2

    while len(str(second_previous)) < length:
        next_number = first_previous + second_previous
        first_previous, second_previous = second_previous, next_number
        position += 1

    return position

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)