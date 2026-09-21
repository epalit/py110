"""
Return the maximum rotation of an int by rotating the number, then fixing the
start digit(s) from 1 until only 2 digits are left and rotating the number. Each
rotation is performed on the result of previous rotations.

Input: number
Output: maximum rotation of the number

Algorithm:
1. Loop over a range from length of str(number) to 1
2. For each iteration, call rotate_rightmost_digits and assign the result to number
3. Return the final result
"""

def max_rotation(number):
    for position in range(len(str(number)), 1, -1):
        number = rotate_rightmost_digits(number, position)

    return number


def rotate_rightmost_digits(number, position):
    if position == 1:
        return number

    str_number = str(number)
    idx = -position

    result = str_number[:idx] + str_number[idx + 1:] + str_number[idx]

    return int(result)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True