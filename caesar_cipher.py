import re, nltk
from corpus_loader import word_list, name_list


def encrypt(plain, shift):
    encrypted = ""

    for char in plain:
        if char.isupper():
            ord_char = ord(char)
            shifted_char = (ord_char + shift - 65) % 26 + 65
            encrypted += chr(shifted_char)
        elif char.islower():
            ord_char = ord(char)
            shifted_char = (ord_char + shift - 97) % 26 + 97
            encrypted += chr(shifted_char)
        else:
            encrypted += char

    return encrypted


def decrypt(cipher, shift):
    return encrypt(cipher, -shift)


def crack(cipher):
    key = 26
    potential_phrase = ""

    while key != 0:
        potential_phrase = decrypt(cipher, key)
        if not check_valid(potential_phrase):
            key -= 1
        else:
            return potential_phrase

    return ""


# ******** HELPER METHODS *********
def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            # print("english word", word)
            word_count += 1
        else:
            # print('not english word or name', word)
            pass

    return word_count


def check_valid(text):
    word_count = count_words(text)

    percentage = int(word_count / len(text.split()) * 100)
    if percentage > 90:
        return True
    else:
        return False
