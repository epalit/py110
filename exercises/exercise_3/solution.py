def is_palindrome(input_string):
    reverse_string = ''.join(reversed(input_string))
    return input_string == reverse_string

def is_real_palindrome(input_string):
    new_str = ''

    for char in input_string:
        if char.isalnum():
            new_str += char

    new_str = new_str.casefold()

    return is_palindrome(new_str)

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

print(is_real_palindrome('Madam') == True)           # True

print(is_real_palindrome("Madam, I'm Adam") == True) # True