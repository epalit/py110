def reverse_number(num):
    reversed_str = ""
    for digit in str(num):
        reversed_str = digit + reversed_str
    return int(reversed_str)

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True