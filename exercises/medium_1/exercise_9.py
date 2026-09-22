"""
Write a function that returns the nth number in the Fibonacci series using 
memoization.

Input: int representing the position of the required Fibonacci number
Output: int representing the Fibonacci number

Requirements:
- Calculate the Fibonacci number at the provided position using the following:
- F(1) = 1, F(2) = 1, F(n) = F(n - 1) + F(n - 2) (where n > 2)
- assume the function is always passed an int > 0
- use memoization rather than computing values that have already been computed

Algorithm:
- create global dictionary storing the fibonacci numbers at different positions
- add 1: 1 and 2: 1 to the global dictionary
- check if the number is in the global dictionary, if yes, return the value
- if no, return fibonacci(number - 1) + fibonacci(number - 2)
"""

FIBONACCI_NUMBERS = {
    1: 1,
    2: 1,
}

def fibonacci(number):
    if number in FIBONACCI_NUMBERS:
        return FIBONACCI_NUMBERS[number]

    FIBONACCI_NUMBERS[number] = fibonacci(number - 1) + fibonacci(number - 2)

    return FIBONACCI_NUMBERS[number]

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True