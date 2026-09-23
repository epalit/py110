"""
Write a function that merges two sorted lists into a single sorted list

Input: two lists of either integers or strings
Output: single list containing the elements from the two provided list in 
ascending order

Rules:
- do not mutate the input lists
- return a new list
- the output list cannot be sorted after construction
- the output list must be built one element at a time in the correct order
- the lists can be different sizes
- the lists can be empty

Algorithm
1. Initialise two pointers to 0 - one for each list, and output list to []
2. while at least one pointer is less then length of their respective lists
    a. if both pointers are less than the length of their lists
        i. select the lowest value from the list and append to output
        ii. increment that pointer by 1
    b. else if first pointer is less than the length of its list
        i. append that value
        ii. increment pointer by 1
    c. else
        i. append value from second list
        ii. increment pointer by 1
3. return output list
"""

def reached_end_of_list(lst, pointer):
    return pointer >= len(lst)

def merge(lst1, lst2):
    lst1_index = 0
    lst2_index = 0
    output = []
    lst1_done = reached_end_of_list(lst1, lst1_index)
    lst2_done = reached_end_of_list(lst2, lst2_index)

    while not lst1_done or not lst2_done:
    
        if not lst1_done and not lst2_done:
    
            if lst1[lst1_index] <= lst2[lst2_index]:
                output.append(lst1[lst1_index])
                lst1_index += 1
            else:
                output.append(lst2[lst2_index])
                lst2_index += 1

        elif not lst1_done:
            output.append(lst1[lst1_index])
            lst1_index += 1

        else:
            output.append(lst2[lst2_index])
            lst2_index += 1

        lst1_done = reached_end_of_list(lst1, lst1_index)
        lst2_done = reached_end_of_list(lst2, lst2_index)

    return output
            

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)