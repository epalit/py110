def leading_substrings(string):
    result = []
    for i in range(1, len(string) + 1):
        result.append(string[:i])
    return result

def substrings(string):
    result = []
    for i in range(len(string)):
        result.extend(leading_substrings(string[i:]))
    return result

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True