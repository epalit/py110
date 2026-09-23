"""
Write a function that returns the transpose of a 3x3 matrix

Input: list of 3 lists with 3 elements each
Output: new list of 3 lists with the rows transposed to columns

Rules:
- the input list(s) must not be modified
- a new list must be returned
- transposing is turning the rows into the columns
- do not use external libraries

Assumptions:
- assume the input will always be a 3x3 matrix

Algorithm:
1. initialise output list as a list with three empty lists as elements
2. iterate over the input matrix
    a. for each nested list
    b. iterate over the elements of the list
    c. add them as the elements of the empty lists in the output
3. return the output
"""

def transpose(matrix):
    output = [[], [], []]

    for row in matrix:
        for idx, element in enumerate(row):
            output[idx].append(element)

    return output

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True