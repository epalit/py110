## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input: string of words separated by spaces
output: string with first and last letter of each word swapped

rules:
  explicit requirements:
    - every word contains at least one letter
    - string will contain at least one word
    - strings only contain words and spaces
    - no leading. trailing or repeated spaces
  implicit requirements:
    - case is irrelevant

questions:
  - what are the rules for non-alpha characters? (assume there won't be any)

assumptions:
  - words are alpha characters only (inferred from use of "letter")
```

## E: Examples / Test cases
```python
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*
Split the string into a list, build new strings into a new list, join the list to get the output string

## A: Algorithm
1. Split string into a list and assign to a variable
2. Initialise a variable with empty list
3. Loop over substring elements
4. Get a new string with the first and last characters swapped
5. Append new string to new list
6. Join list into string
7. Return string

swapped string:
input: word
output: word with first and last letter swapped

1. Concatenate new string using last index, middle slice, first index
2. Return string
## C: Code
```bash
python solution.py
```
