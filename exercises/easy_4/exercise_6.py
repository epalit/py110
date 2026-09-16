def leading_substrings(string):
    result = []
    for i in range(1, len(string) + 1):
        result.append(string[:i])
    return result

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])