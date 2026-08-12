
def sort_by_consonant_count(string_list):
    adjacent_consonant_counts = {}
    for string in string_list:
        count = count_adjacent_consonants(string)

        if count in adjacent_consonant_counts:
           adjacent_consonant_counts[count].append(string)
        else:
            adjacent_consonant_counts[count] = [string]

    result = []
    while adjacent_consonant_counts:
        max_count = max(adjacent_consonant_counts)
        result.extend(adjacent_consonant_counts.pop(max_count))

    return result


def count_adjacent_consonants(string):
    max_adj_consonant_count = 0
    consonant_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    string = ''.join(string.split()).lower()

    for char in string:
        is_consonant = char.isalpha() and char not in vowels
        if is_consonant:
            consonant_count += 1
            if consonant_count >= 2:
                max_adj_consonant_count = max(consonant_count, max_adj_consonant_count)
        else:
            consonant_count = 0

    return max_adj_consonant_count

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])

my_list = ['ab', 'bbba', 'bbabbbb']
print(sort_by_consonant_count(my_list) == ['bbabbbb', 'bbba', 'ab'])