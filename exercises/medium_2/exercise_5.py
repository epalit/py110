"""
Write a function that returns the next "featured" number or returns an error
string if there isn't one.

Input: int
Output: int or error message string

Rules:
- a featured number:
  - is odd
  - is a multiple of 7
  - all its digits do not occur more than once
- the next featured number greater than the argument should be returned
- the largest possible featured number is 9876543201
- will assume the argument will always be a positive integer

Original Algorithm:
1. check the number is less than 9876543201 otherwise return error str
2. iterate from number to 9876543201
3. for each iteration check if the number:
  a. is odd
  b. is multiple of 7
  c. doesn't have any duplicate digits
    i. seen = set()
    ii. iterate over str of number
    iii. for each iteration, if digit is in seen, return True
    iv. add digit to seen
    v. return False at end
4. if any criteria isn't met, continue
5. if all criteria are met return the number
6. if the end of the loop is reached return error string

(updated implementation to use more efficient method from solution)
"""
ERROR_MSG = "There is no possible number that fulfills those requirements."
LARGEST_FEATURED_NUM = 9876543201

def get_next_odd_multiple_of_7(number):
    if is_odd_multiple_of_7(number):
        number += 14
    else:
        number += 1
        while not is_odd_multiple_of_7(number):
            number += 1

    return number

def is_odd_multiple_of_7(number):
    return (number % 2 == 1) and (number % 7 == 0)

def has_duplicate_digits(number):
    seen = set()
    for digit in str(number):
        if digit in seen:
            return True
        seen.add(digit)
    return False

def next_featured(number):
    if number >= LARGEST_FEATURED_NUM:
        return ERROR_MSG

    while number < LARGEST_FEATURED_NUM:
        number = get_next_odd_multiple_of_7(number)
        if not has_duplicate_digits(number):
            return number

    return ERROR_MSG
         
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True

