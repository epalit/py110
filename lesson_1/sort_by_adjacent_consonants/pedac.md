## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

```text
input: list of strings
output: return sorted list (based on highest number of adjacent consonants)

rules:
  explicit requirements:
    - list should be sorted based on the highest number of adjacent consonants each string contains
    - if two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other
    - adjacent means:
      - consonants are next to eachother in the same word OR
      - consonants are either side of a space between adjacent words
  implicit requirements:
    - strings may contain multiple words
    - sort order is descending (most adjacent to least)
    - if there are multiple strings with no adjacent consonants, order should be as they are in the list (test case 1)
    - empty list input results in empty list output
    - words are seperated by whitespace
    - strings may not be empty
    - case is not relevant
    - consonants separated by non-alpha chars are not adjacent

questions:
  - should empty list input return empty list?
    - not answered by test cases, assume yes
  - does the returned object need to be a new list or mutated input?
    - not specified, decide on implementation
  - should punctuation count as separators for words (like space)?
    - not in test cases, assume no, and that nonalpha chars prevent adjacency
  - do all whitespace characters count as space or is a single space expected?
    - test cases only cover single space, assume any whitespace counts
  - case insensitive?
    - test cases are all lowercase, assume case can be ignored
  - asc or desc sort order?
    - answered by test cases
```

## E: Examples / Test cases

```python
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
```

## D: Data Structure
*Make notes, does not have to be final on the first pass*

- A list will be required as the returned object
- A dictionary may be useful to keep count of the adjacent consonants

## A: Algorithm

1. Create an empty dictionary to store how many adjacent consonants for each word
  a. keys are the count
  b. values is a list of words with that count
2. Loop over the list and
  a. count the adjacent consonants
  b. add the string to the list (value) paired with the count (key)
3. Initialise a new list
4. Get the value associated with the max count from the dictionary
5. Append it to the new list
6. Remove the k/v from the dict
7. Loop 4 and 5 until no keys are left
8. Return the new list

## count adjacent consonants:
input: string

output: int (max run of consonants in the string)

1. Set max consonant run to 0
2. Set consonant count to 0
3. Set vowels list
4. Remove whitespace from string and lower it
5. Loop over string
6. if char is a consonant
  a. increment count by one
  b. if count 2 or more, set the max to the new count if it is larger than the existing max
7. if char is not a consonant
  a. reset count
8. return the max length found

## C: Code
```bash
python solution.py
```