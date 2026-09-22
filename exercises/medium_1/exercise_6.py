"""
Write a function that determines whether a number is prime.

input: int (positive)
output: bool representing whether the number is prime

rules:
- a number is prime if it is only divisible by itself and 1
- 1 is not prime
- do not use any add-on packages

algorithm:
1. if the number is 1 return False
2. loop over the range 2 -> number - 1
3. for each iteration check if number % divisor is 0
4. if yes, return False
5. after the loop return True
"""

def is_prime(number):
    if number == 1:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True