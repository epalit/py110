"""
Write a function that calculates the number that is needed to add to a given
list of numbers so the new list sums to the next prime numnber along from the
sum of the previous list

Input: list of ints
Output: int

Rules:
- The list will always contain at least 2 integers.
- All values in the list must be positive (> 0).
- There may be multiple occurrences of the various numbers in the list.

Algorithm:
1. Sum the list
2. Find the next prime number
    a. starting from the sum of the list + 1, iterate in steps of 1
    b. each iteration
        i check whether the number is prime
            1. if the number is 1, return False
            2. iterate on a range up to the number
            3. if the number is divisible then return False
            4. end return True
        ii. if yes return it
        iii. if no increment by 1
3. return the difference
"""

def is_prime(number):
    if number == 1:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True

def get_next_prime(number):
    number += 1
    while True:
        if is_prime(number):
            return number

        number += 1

def nearest_prime_sum(numbers):
    numbers_total = sum(numbers)

    next_prime = get_next_prime(numbers_total)

    return next_prime - numbers_total

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)