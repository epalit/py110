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
    - first player to win configurable number of games wins the match
    - reset scores to 0 for both players at the start of a match
    - don't use global variables except for configuration constants
    - set configuraiton to 5 games wins a match
  implicit requirements:
    -

questions:
  -

assumptions:
  - continue to ask if the player wants to play again after each game
  - we should display ties as well as wins
```

## E: Examples / Test cases
```python
```

## D: Data Structure
*Make notes, does not have to be the final version on the first pass*
- keep score in a dictionary {"player" : 0, "computer" : 0, "ties": 0}

## A: Algorithm
1. reset scores at the start
2. display scores every time a board is displayed
3. record result when it is known
4. check if there is a match winner after each game concludes
5. ask to play again after each game

**see keep_score.drawio**

## C: Code
