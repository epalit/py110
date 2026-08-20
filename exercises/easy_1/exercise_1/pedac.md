# Searching 101

## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input: 6 numbers
output: print msg describing whether the sixth number appears among the first five
rules:
  explicit requirements:
    - user will provide 6 numbers
    - check for the presence of the 6th number in the first 5
  implicit requirements:
    - user inputs 6 numbers sequentially
    - prompt the user one at a time
    - prompt specifies which number (1st, 2nd...last)
    - print message follows a specific format including printed the numbers in order
questions:
    1. ints only? Will assume yes
assumptions:
    - user will always enter integers
```

## E: Examples / Test cases
```python
"""Example 1"""
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

"""Example 2"""
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*
- gather the inputs as a list: this can be used in the output message (order is preserved)

## A: Algorithm
1. Create empty list for input numbers
2. Ask for a number using the appropriate message
2. Append to number list
3. repeat 4 more times
4. ask for final number
5. check if final number in constructed list
6. print message saying whether the number was or wasn't there

## C: Code
```bash
python solution.py
```