"""
# Problem
Find the digit count positions from the end of the provided number, and move it
to the end of the number.

Input: number and a position (both ints)
Output: int with the digit at position from the end moved to the end

requirements:
- return an int with the selected digit moved to the end
- assume position is in the range of the number provided
- assume will always be provided ints

# Algorithm
1. Convert the number to a string
2. Set idx variable to provided position * -1
3. Assign a variable the concatenation of:
    a. The start of the string to idx
    b. from idx + 1 to the end of the string
    c. The element at idx
4. Convert the string to an int and return
"""

def rotate_rightmost_digits(number, position):
    if position == 1:
        return number

    str_number = str(number)
    idx = -position

    result = str_number[:idx] + str_number[idx + 1:] + str_number[idx]

    return int(result)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True