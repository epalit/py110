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

def is_palindrome(string):
    if len(string) < 2:
        return False
    return string == ''.join(reversed(string))

def palindromes(string):
    substring_list = substrings(string)
    return [s for s in substring_list if is_palindrome(s)]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True