"""
# Problem
input: list of integers
output: integer

requirements:
- average the integers in the given list and return the integer component of the result
- round down
- list is never empty
- numbers are always positive integers

# Examples
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

# Data
Process the list and compute the average

# Algorithm
1. sum list
2. integer divde by length of the list
3. return the result
"""

def average(lst):
    return sum(lst) // len(lst)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True