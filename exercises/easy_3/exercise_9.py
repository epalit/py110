"""
# Problem
input: list
output: same list object with elements reversed
requirements:
- return the same object as used as the argument
- do not use list.reverse
- do not use slicing

# Algorithm
1. set start and end index to 0 and -1 respectively
2. get middle index using floor divide
3. loop for range of middle index
4. switch start and end index positions
5. increment start index by one
6. decrement end index by one
7. return list

"""

def reverse_list(lst):
    start_idx = 0
    end_idx = -1
    mid_idx = len(lst) // 2

    for _ in range(mid_idx):
        lst[start_idx], lst[end_idx] = lst[end_idx], lst[start_idx]
        start_idx += 1
        end_idx -= 1

    return lst


list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True