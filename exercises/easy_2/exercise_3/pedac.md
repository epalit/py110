## Problem

- input: list
- output: list of two lists, each with half of the input list (first half bigger if it is odd)

## Examples
```python
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
```

## Data

## Algorithm
1. initialise result list
2. find the midpoint of the list
3. create a list from the elements before the midpoint
4. add to the result list
5. create a list from the elements after and including the midpoint
6. add to the result list
7. return list

### finding the midpoint
1. calculate the length of the list
2. if the length is even return length divided by two
3. if the length is odd, add one and divide the result by two

## Code