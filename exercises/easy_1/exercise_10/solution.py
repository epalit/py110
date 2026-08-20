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

    if num < 10:
        return string_map[num]

    while num > 0:
        digit = num % 10
        num_as_str = string_map[digit] + num_as_str
        num = num // 10

    return num_as_str

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True