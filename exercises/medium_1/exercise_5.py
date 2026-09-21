"""
input: string
output: string with number words converted to digits

algorithm:
1. create a dictionary of number words to digits
2. split the string
3. loop over the resulting list
4. if element matches a key in dict, append the value else appen element
5. return joined list
"""

def word_to_digit(sentence):
    number_words = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    words = sentence.split()

    result = [number_words.get(word, word) for word in words]

    return ' '.join(result)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True