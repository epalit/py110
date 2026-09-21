"""
# Problem
Take a list and move the first element to the end of the list and return it, 
without modifying the original list.

Input: list
Output: new list with the first element of the input list moved to the end

requirements:
- move the first element to the end
- do not mutate the provided list
- empty list -> empty list
- non-list -> None
- single element list -> list with the same element (assume new version of the list)
- assume we don't need new objects for all list elements

# Algorithm
1. Check input is a list, if not, return None
2. Check len of input, if it is 0, return an empty list
3. Assign result variable slice of input list from element in the 2nd position 
onwards plus the element at 0
4. Return the list
"""

def rotate_list(lst):
    if not isinstance(lst, list):
        return None

    if len(lst) == 0:
        return []

    result = lst[1:] + [lst[0]]

    return result

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])