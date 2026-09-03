def find_midpoint(lst):
    return (len(lst) + 1) // 2

def halvsies(nums):
    result = []
    midpoint_idx = find_midpoint(nums)

    first_half = nums[:midpoint_idx]
    result.append(first_half)

    second_half = nums[midpoint_idx:]
    result.append(second_half)

    return result


print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])