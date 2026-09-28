"""
Write a function that calculates the maximum product of four consecutive
digits in a given string

Input: string of digits
Output: int

Rules:
- The argument will always have more than 4 digits

Algorithm:
- set max_product = 0, start_idx = 0, end_idx = 4
- while end_idx <= len(string)
    - get the product of the slice from start to end idx
        - product = 1
        - for digit in string
        - product *= int(digit)
    - if the product is greater than the max, store it
    - increment both indicies by 1
- return max_product
"""

def get_product(string):
    product = 1

    for digit in string:
        product *= int(digit)

    return product

def greatest_product(number):
    max_product = 0
    start_idx = 0
    end_idx = 4

    while end_idx <= len(number):
        product = get_product(number[start_idx:end_idx])

        if product > max_product:
            max_product = product

        start_idx += 1
        end_idx += 1

    return max_product

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6