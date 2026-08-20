def integer_to_string(num):
    string_map = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
    }
    num_as_str = ''

    if num == 0:
        return "0"

    while num > 0:
        digit = num % 10
        num_as_str = string_map[digit] + num_as_str
        num = num // 10

    return num_as_str

def signed_integer_to_string(num):
    if num == 0:
        return "0"
    elif num > 0:
        return '+' + integer_to_string(num)
    else:
        return '-' + integer_to_string(num * -1)

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True