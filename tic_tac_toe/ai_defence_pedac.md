## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input:
output:

rules:
  explicit requirements:
    - if the human player has 2 squares in a row with the 3rd unoccupied, computer picks the unoccupied square
  implicit requirements:
    - 

questions:
  -

assumptions:
  - if there are multiple immediate threats, pick one at random
  - make the AI intelligence configurable
```

## E: Examples / Test cases
```python
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*

## A: Algorithm
1. find immediate threats
  a. initialist empty list of threat squares
  b. build lines (list of lists)
  c. iterate over lines
  d. for each line look for a threat square
    i. if one initial marker is present, check for two player markers
    ii. else return None
  e. if present, add index of initial markers to list of threats
2. if threats is not empty, pick a threat square at random as the choice
3. otherwise pick a random available square

## C: Code
```bash
python solution.py
```
