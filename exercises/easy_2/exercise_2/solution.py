def union(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    return set_1 | set_2

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True