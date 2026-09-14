"""
# Problem
input: string
output: string with each char doubled

# Examples
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

#Algorithm
1. In a list comp, for each char, double it
3. Join the list back up and return it
"""

def repeater(text):
    char_list = [char * 2 for char in text]
    return "".join(char_list)

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True