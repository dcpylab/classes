#-*- coding: utf-8 -*-
# Bilingual dictionary: take a phrase in one
# language and translate it one word at a time
# into another. In this case, we're using:
# Spanish
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

translations = {
    "merry": "feliz",
    "christmas": "navidad",
    "and": "y",
    "happy": "feliz",
    "new": "nuevo",
    "year": "año",
}

phrase = input("Please enter a phrase: ")

spanish_phrase = []
for word in phrase.split():
    word = word.lower()
    spanish_word = translations.get(word, word)
    spanish_phrase.append(spanish_word)

separator = " "
spanish_phrase = separator.join(spanish_phrase)
print("In Spanish, that's:", spanish_phrase)
