## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input: string
output: dictionary of number of words of different sizes

rules:
  explicit requirements:
    - string contains zero or more space-separated words
    - words are any sequence of non-space characters
    - count the words of different lengths
  implicit requirements:
    - dictionary keys are word length
    - dictionary values are counts as integers
    - empty string results in empty dictionary

questions:
  -

assumptions:
  - 
```

## E: Examples / Test cases
```python
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*
Build a dictionary as this will be returned

## A: Algorithm
1. Split the string into words in a list
2. Create an empty dict for the counts
3. Iterate over the list
4. Increment the count for the length of the word for each word
5. Return the dictionary

## C: Code
```bash
python solution.py
```
