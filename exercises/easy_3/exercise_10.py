"""
# Problem
input: string
output: bool - True if all parentheses in the string are matched, otherwise False
# Algorithm
1. Initialise count of unmatched opening parentheses to 0
2. Loop over string
3. if char is (, increment count by one
4. if char is )
  a. if ( count is greater than zero, decrement by 1 otherwise return False
5. if at the end of the loop ( count is above zero, return False
6. Return True
"""

def is_balanced(string):
    unmatched_open_parentheses = 0
    for char in string:
        if char == '(':
            unmatched_open_parentheses += 1
        elif char == ')':
            if unmatched_open_parentheses > 0:
                unmatched_open_parentheses -= 1
            else:
                return False

    return unmatched_open_parentheses == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True