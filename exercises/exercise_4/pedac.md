## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input: list of numbers
output: list with each element being the running total from the input list

rules:
  explicit requirements:
    - returned list has the same number of elements
  implicit requirements:
    - list of size one returns the same list
    - empty list returns list

questions:
  - will all elements always be ints? (assume yes)

assumptions:
  - all list elements will be integers
```

## E: Examples / Test cases
```python
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*
Will need to create a new list to hold the running totals and append as we go
Use an integer to maintain a running total

## A: Algorithm
1. Create variable for totals list and assign it empty list
2. Create a variable for the running total and assign it 0
3. Loop over input list and for each element:
  a. Add the element to the running total
  b. Append to the total to the new list
4. Return the new list

## C: Code
```bash
python solution.py
```
