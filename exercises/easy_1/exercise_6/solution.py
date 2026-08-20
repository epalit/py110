def word_sizes(words):
    word_list = words.split()

    counts = {}
    for word in word_list:
        new_word = ''.join(char for char in word if char.isalpha())
        word_len = len(new_word)
        if word_len > 0:
            current_count = counts.get(word_len, 0)
            counts[word_len] = current_count + 1

    return counts

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

print(word_sizes('!!!') == {})