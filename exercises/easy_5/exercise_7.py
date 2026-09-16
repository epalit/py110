def sum_digits(number):
    total = 0
    for digit_str in str(number):
        total += int(digit_str)
    return total

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True