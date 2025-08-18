def word_counter(text):
    num_words = len(text.split())
    return num_words

def character_counter(text):
    lowercase = text.lower()
    alphabet = {}
    for letter in lowercase:
        if letter not in alphabet:
            alphabet[letter] = 1
        else:
            alphabet[letter] += 1
    return alphabet

def sort_on(items):
    return items["num"]

def sort_char(alphabet):
    cleaned_alphabet = []
    for char in alphabet:
        count = alphabet[char]
        new_dict = {"char": char, "num": count}
        cleaned_alphabet.append(new_dict)
    cleaned_alphabet.sort(reverse=True, key=sort_on)
    return cleaned_alphabet