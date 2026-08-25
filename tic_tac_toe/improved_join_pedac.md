## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

- Template:
```text
input:
  - list of items to join
  - optional separator
  - optional final separator
output:
  - string of elements joined by separator and a final separator
rules:
  explicit requirements:
    - join the elements with the provided separators
  implicit requirements:
    - default separator is ','
    - default final separator is ' or '
    - empty list returns empty string
    - single element results in no separators being included
    - two elements use the final separator only

questions:
  -

assumptions:
  - 
```

## E: Examples / Test cases
```python
print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*

## A: Algorithm
1. Check for empty list and return ""
2. Check for single element and return it as a string
3. Check for two elements and return them joined with the final separator
4. Remove the final element from the list and save into a variable
5. Join the remaining elements with the separator
6. Concatenate (5) with the final separator and the saved last element
7. Return the concatenated string

## C: Code
```python
def join_or(elements, sep=',', final_sep='or'):
  if len(elements) == 0:
    return ""

  if len(elements) == 1:
    return str(elements[0])

  if len(elements) == 2:
    return f" {final_sep} ".join(str(e) for e in elements)

  last_element = elements.pop()
  elements_str = f"{sep} ".join(str(e) for e in elements)
  return f"{elements_str} {final_sep} {last_element}"
```
