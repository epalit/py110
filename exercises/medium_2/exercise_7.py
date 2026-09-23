"""
Write a function that sorts a list in place using the bubble sort algorithm

Input: list of ints
Output: returns None, list sorted in place as side effect

Rules:
- pass over the list swapping elements where the largest of the pair is first
- continue passes until no swaps are made in a pass
- assume list has at least two elements

Algorithm:
1. Set a flag swapped = True
2. Set up a while loop until swapped is False
3. for each iteration:
  a. set swapped to False
  b. do any required swaps, setting swapped to True
    i. iterate over range 1 to length of list
    ii. if first elemement > second, swap and set flag to True
  c. set length to n - 1
"""

def bubble_sort(numbers):
    swapped = True
    n = len(numbers)

    while swapped:
        swapped = False

        for idx in range(1, n):
            if numbers[idx - 1] > numbers[idx]:
                numbers[idx - 1], numbers[idx] = numbers[idx], numbers[idx - 1]
                swapped = True
        n -= 1


lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True