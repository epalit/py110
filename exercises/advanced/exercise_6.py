"""
Write a function that implements a binary search

Input: list and search item
Output: index of the search item if found or -1

Rules:
- assume the list is sorted

Algorithm:
1. calculate midpoint of the list
2. retrieve the value at the midpoint index
3. if it is the search term, return the index
4. if it is less than the search term
  i. discard everything from the midpoint and lower
  ii. return midpoint + binary search of (i)
5. if not
  i. return binary search of discard everything from the midpoint and higher
6. search the remaining list
7. return starting index + index of located item
"""

def binary_search(lst, item):
    if len(lst) == 0:
        return -1

    mid_idx = len(lst) // 2
    mid_value = lst[mid_idx]

    if mid_value == item:
        return mid_idx

    if mid_value < item:
        start_idx = mid_idx + 1
        next_idx = binary_search(lst[start_idx:], item)
        return next_idx if next_idx == -1 else start_idx + next_idx

    return binary_search(lst[:mid_idx], item)
    

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)