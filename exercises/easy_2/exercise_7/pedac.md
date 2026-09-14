# Problem

Input: two lists of numbers
Output: a new list with the product of each number from corresponding index positions in the input lists

requirements:
- assume input lists are the same length
- assume lists only contain numbers

# Examples
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

# Data
Build a list

# Algorithm
1. zip through list one and two
2. multiply each element pair