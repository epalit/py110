## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input: integer
output: string representing the integer

rules:
  explicit requirements:
    - cannot use `str`
    - input will not be negative
  implicit requirements:
    - none

questions:
  - none

assumptions:
  - none
```

## E: Examples / Test cases
```python
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*
Use a dictionary to create a map of ints to string
Build a string to return

## A: Algorithm
1. Intialise a dictionary mapping int digits to str digits
2. Initialise return string as empty string
3. Modulo divide number by 10
4. Lookup the string and concatenate to the start of return string
5. Integer divide number by 10 and set num to result
6. Stop when number hits 0
7. return string

## C: Code
```bash
python solution.py
```
