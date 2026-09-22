"""
Write a function that returns the nth number in the Fibonacci series.

Input: int representing the position of the required Fibonacci number
Output: int representing the Fibonacci number

Requirements:
- Calculate the Fibonacci number at the provided position using the following:
- F(1) = 1, F(2) = 1, F(n) = F(n - 1) + F(n - 2) (where n > 2)
- assume the function is always passed an int > 0

Algorithm:
- If number is 1 or 2, return 1
- return fibonacci(number - 1) + fibonacci(number - 2)
"""

def fibonacci(number):
    if number <= 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True