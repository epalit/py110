"""
# Problem
input: list
output: print each element and its count

requirements:
- words are case sensitive
- output print format is element => count
- order of printing elements does not matter

# examples
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2

# data:
store counts in a dictionary

algorithm:
1. count elements
  a. create a dictionary to store counts
  b. loop over list
  c. if element is in the dict, increment count by 1, else add it with value of 1
2. print result
  a. loop of dict printing key => val for each item
"""

def count_occurrences(lst):
    counts = dict()

    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for key, val in counts.items():
        print(f"{key} => {val}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)