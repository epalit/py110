"""
Write a function that returns a list of the count of numbers in the original list
that are smaller than the number at the same position in the original list

Input: list of ints
Output: list of ints representing the count of smaller numbers

Rules:
- only count unique values

Assumptions:
- assume the list only contains integers
- assume the list won't be empty

Algorithm
- set output to empty list
- iterate over enumerated original list
- set count to 0
- take a copy of the list
- pop the item at idx and save it
- create a set from the remaining items in the copied list
- iterate over the set counting items less than popped item
- append count to output list
- return output
"""

def smaller_numbers_than_current(numbers):
    unique_numbers = set(numbers)
    output = []

    for num in numbers:
        count = 0

        for unique_num in unique_numbers:
            if unique_num < num:
                count += 1

        output.append(count)

    return output
        
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)