"""
Write a function that performs a merge sort on a list

Input: list of elements of the same type
Output: new sorted list

Rules:
- do not mutate input list
- follow this algorithm:
  - split the list into two until the innermost lists contain one element only
  - merge pairs of lists using the merge function from exercise 4
  - continue until the list is back to a single list of elements (not nested)

Algorithm:
1. base case - if list length 1 or 0, return it
2. find the midpoint (integer divide len list + 1 by 2)
3. use slicing to create two sublists based on midpoint
4. return merge of the merge_sort of the two sublists
"""

def merge(list1, list2):
    copy1 = list1[:]
    copy2 = list2[:]
    result = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))

    return result + copy1 + copy2

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    midpoint = (len(lst) + 1) // 2

    return merge(merge_sort(lst[:midpoint]), merge_sort(lst[midpoint:]))

# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)