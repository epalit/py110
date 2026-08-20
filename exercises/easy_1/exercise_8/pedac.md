## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input: string of digits
output: int representing the number from the string

rules:
  explicit requirements:
    - do not use Python standard conversation functions like `int`
    - calculate the result from the string characters
    - assume string is all numeric characters
  implicit requirements:
    - none

questions:
  - none

assumptions:
  - none
```

## E: Examples / Test cases
```python
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*
Constant 48 to convert ord to the int

## A: Algorithm
1. Initialise a variable for the output number and set it to 0
2. Loop over enumeration of the string
3. Convert each item to integer plus zeros representing it's base 10 position
4. Add this integer to the output variable
5. Return the variable

Conversion:
1. Take a single digit string, a position and a string length
2. Get the ord of the string
3. Minus 48 from the ord
4. Multiply the result by 10 to the power length of string -1 -position
5. Return the result

## C: Code
```bash
python solution.py
```
