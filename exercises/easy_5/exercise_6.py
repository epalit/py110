def get_subsequences(nums):
    subsequences = []
    for end_idx in range(1, len(nums)+1):
        subsequences.append(nums[:end_idx])
    return subsequences

def sum_of_sums(nums):
    subsequences = get_subsequences(nums)
    sums = [sum(items) for items in subsequences]
    return sum(sums)

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True