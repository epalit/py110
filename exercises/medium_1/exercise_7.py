"""
Write a function that returns the nth number in the Fibonacci series.

Input: int representing the position of the required Fibonacci numnber
Output: int representing the Fibonacci number

Requirements:
- Calculate the Fibonacci numner at the provided position using the following:
- F(1) = 1, F(2) = 1, F(n) = F(n - 1) + F(n - 2) (where n > 2)
- assume the function is always passed an int > 0

Algorithm:
- If number is 1 or 2, return 1
- initialise dictionary with 1: 1, and 2: 1
- iterate over range 3 to number + 1
- for each iteration, sum the values in the dictionary for the prior two numbers
and add the result as the value to the diction for that number
- return the value from the dictionary with the key of the provided number
"""

def fibonacci(position):
    if position <= 2:
        return 1

    fibonacci_numbers = {
        1: 1,
        2: 1,
    }

    for num in range(3, position + 1):
        fibonacci_numbers[num] = (
            fibonacci_numbers[num - 1] + fibonacci_numbers[num - 2]
        )

    return fibonacci_numbers[position]

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True