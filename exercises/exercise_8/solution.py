ORD_ZERO = ord('0')
ORD_A_MINUS_TEN = ord('A') - 10

def string_to_integer(num):
    num_as_int = 0

    for idx, digit in enumerate(num):
        num_as_int += get_digit_as_int(digit, idx, len(num))

    return num_as_int

def get_digit_as_int(digit, position, length):
    return (ord(digit) - ORD_ZERO) * (10 ** (length - 1 - position))

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

def hexadecimal_to_integer(num):
    num_as_int = 0

    for idx, digit in enumerate(num):
        num_as_int += get_hex_as_int(digit, idx, len(num))

    return num_as_int

def get_hex_as_int(digit, position, length):
    if digit.isdigit():
        hex_digit = ord(digit) - ORD_ZERO
    else:
        hex_digit = ord(digit.upper()) - ORD_A_MINUS_TEN

    return hex_digit * (16 ** (length - 1 - position))

print(hexadecimal_to_integer('1A') == 26)  # True
print(hexadecimal_to_integer('4D9f') == 19871)  # True