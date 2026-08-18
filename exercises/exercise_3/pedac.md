## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input: string
output: boolean - `True` for palindrome, `False` for not

rules:
  explicit requirements:
    - case-insensitive
    - ignore all non-alphanumeric characters
  implicit requirements:
    -

questions:
  -

assumptions:
  - 
```

## E: Examples / Test cases
```python

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*
Will need to create a new string with non-alphanumeric chars removed and lower it

## A: Algorithm
1. Create a variable and assign it an empty string
2. Loop over input string and add only alphanumeric strings to the new string
3. lowercase the new string
4. Check if the new string is a palindrome
5. Return result

## C: Code
```bash
python solution.py
```
