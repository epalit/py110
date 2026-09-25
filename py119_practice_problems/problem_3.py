"""
Write a function that converts every 2nd character in every 3rd word to uppercase

Input: string
Output: string

Rules:
- all other characters remain the same

Assumptions:
- if a character is not an alpha, it will not be uppercased
- the string will contain words separated by whitespace

Algorithm:
- split the string into a list of words
- iterate over the words list with enumerate starting at 1
    - for each iteration, if the position is divisible by 3:
        - get the uppercased version
        - replace the word in the list with the uppercased version
- return " ".join(words)

Uppercasing:
  - result = ""
    - iterate over string with enumerate
    - if idx % 2 == 0
        - uppercase the char
    - add char to result
  - return string
"""

def uppercase_every_2nd(word):
    result = ""

    for idx, char in enumerate(word):
        if idx % 2 == 1:
            char = char.upper()
        result += char

    return result

def to_weird_case(words):
    words_list = words.split()

    for pos, word in enumerate(words_list, start=1):
        if pos % 3 == 0:
            words_list[pos - 1] = uppercase_every_2nd(word)

    return " ".join(words_list)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)