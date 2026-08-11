## P: Understand the Problem
- Read the problem description
- Check any test cases
- Ask clarifying questions if anything is unclear

```text
input: integer (number of blocks)
output: return an integer (number of blocks leftover)

rules:
  explicit requirements:
    - the structure is built in layers of blocks
    - blocks are cubes
      - cubes are 6-sided square face
    - top layer is a single block
    - each upper layer block must be supported by four blocks in a lower layer
    - a lower layer block can support more than one upper layer block
    - no gaps between blocks
    - the tallest possible structure should be built
    - the structure must be valid
    - calculate the blocks leftover
  implicit requirements:
    - second layer must be 4 blocks
    - zero provided blocks results in zero leftover
    - pattern is:
      - each layer is a square
      - each layer side length is one more than the upper layer

questions:
  - Is a lower layer valid if it has more blocks than it needs? (no, see 6th test case)
  - Will there always be leftover blocks? (no)
```

## E: Examples / Test cases

```python
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
```

## D: Data Structure
*Make notes, does not have to be final on the first pass*

- Order is important
- Layers of numbers of blocks

Perhaps we can use a list where each element is the number of blocks in the row. Row 0 (i.e. the first element) always has to be 1 and represents the top layer.

## A: Algorithm

1. Set the number of blocks leftover to be the total blocks given
2. Set structure to empty list
3. Set layer number to 1
4. Calculate the blocks needed for the layer (layer ** 2)
5. If leftover blocks is greater than or equal to the required blocks:
  a. Append required blocks to structure list
  b. Subtract required blocks from the leftover
6. If not, return the leftover blocks
7. Increment layer by one and repeat 4-6

## C: Code
```bash
python solution.py
```