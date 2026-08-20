def swap(sentence):
    word_list = sentence.split()
    new_words = []

    for word in word_list:
        new_words.append(get_swapped_word(word))

    new_sentence = ' '.join(new_words)

    return new_sentence

def get_swapped_word(word):
    if len(word) == 1:
        return word

    return word[-1] + word[1:-1] + word[0]

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
print(swap('ab') == "ba")                    # True