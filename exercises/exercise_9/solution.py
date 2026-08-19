ORD_ZERO = ord('0')

def string_to_integer(num):
    num_as_int = 0

    for idx, digit in enumerate(num):
        num_as_int += get_digit_as_int(digit, idx, len(num))

    return num_as_int

def string_to_signed_integer(num):
    num_is_negative = False

    if num[0] == '-':
        num_is_negative = True
        num = num[1:]
    elif num[0] == '+':
        num = num[1:]

    num_as_int = string_to_integer(num)

    if num_is_negative:
        num_as_int *= -1

    return num_as_int

def get_digit_as_int(digit, position, length):
    return (ord(digit) - ORD_ZERO) * (10 ** (length - 1 - position))

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True