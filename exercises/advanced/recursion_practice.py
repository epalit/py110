def sum_digits(number):
    if number // 10 == 0:
        return number

    return number % 10 + sum_digits(number // 10)

print(sum_digits(1234) == 10)  # → 10
print(sum_digits(507) == 12)   # → 12
print(sum_digits(12) == 3)     # → 8
print(sum_digits(8) == 8)     # → 8

def reverse_string(string):
    if len(string) == 0:
        return string

    return reverse_string(string[1:]) + string[0]

print(reverse_string("hello") == "olleh")   # → "olleh"
print(reverse_string("Python") == "nohtyP") # → "nohtyP"
print(reverse_string("a") == "a")      # → "a"
print(reverse_string("") == "")       # → ""

def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n-1)

count_down(5)

def count_up(n):
    if n == 0:
        return

    count_up(n-1)
    print(n)

count_up(5)

def sum_to(n):
    if n == 0:
        return n
    return n + sum_to(n-1)

print(sum_to(5))

def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent-1)

print(power(2, 4))  # 16
print(power(5, 3))  # 125
print(power(7, 0))  # 1

def sum_list(numbers):
    if len(numbers) <= 1:
        return 0 if not numbers else numbers[0]

    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4]) == 10) # 10
print(sum_list([5]) == 5)            # 5
print(sum_list([]) == 0)             # 0