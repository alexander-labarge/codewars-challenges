def anagrams(word, words):
    result = []
    starting_word = word
    starting_words = words.copy()
    convert_starting_word = convert_x(word)
    convert_starting_words = convert_y(words)
    i = 0
    for word in convert_starting_words:
        if word == convert_starting_word:
            result.append(starting_words[i])
            i += 1
        else:
            i += 1
    return result  

def convert_x(word):
    search = ''.join(sorted(word))
    return search

def convert_y(words):
    string_list = words
    converted_list = []
    for i in string_list:
        converted_list.append((''.join(sorted(i))))
    return converted_list
