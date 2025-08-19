def get_num_words(text):
    num_words = text.split()
    return len(num_words)

def get_num_characters(text):
    char_dictionary = {}
    lower_text = text.lower()
    characters = lower_text[::]
    for char in characters:
        if char in char_dictionary:
            char_dictionary[char] += 1
            # print(char_dictionary[char])
        else:
            char_dictionary[char] = 1
    return char_dictionary

def sort_on(list):
    return list["num"]

def get_num_characters_sorted(dict):
    revised_list = []

    for entries in dict:
        for entry in entries:
            if entry.isalpha():
                num = dict[entry]
                char = entry
                revised_list.append({"char": char, "num" : num})

    # print(type(revised_list))
    revised_list.sort(reverse=True, key=sort_on)
    return revised_list