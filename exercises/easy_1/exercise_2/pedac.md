## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input: string
output: boolean - `True` if the string is a palindrome `False` if not

rules:
  explicit requirements:
    - palindrome reads the same forwards and backwards
    - case sensitive
    - all characters matter (i.e. include non-alpha and whitespace in checks)
  implicit requirements:
    -

questions:
  -

assumptions:
  - 
```

## E: Examples / Test cases
```python
# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*
should be able to reverse the string to make a new srting object for comparison

## A: Algorithm
1. Create a reverse of the string and store in a variable
2. Compare the original and reverse strings
3. If they are the same return True, if not return False

## C: Code
```bash
python solution.py
```
