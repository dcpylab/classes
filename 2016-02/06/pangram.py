#
# This program recognizes pangrams, e.g. "The quick brown
#  fox jumps over the lazy dog" is a pangram.
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

def is_pangram(sentence):
    """
    Test whether or not the sentence is a pangram, i.e.
    it contains all the letters in the English language.
    """
    all_letters = set("abcdefghijklmnopqrstuvwxyz")

    letters_in_sentence = set()

    for letter in sentence:
        letter = letter.lower()
        letters_in_sentence.add(letter)

    is_it_a_pangram = letters_in_sentence.issuperset(all_letters)
    return is_it_a_pangram

# list_of_things = [1, 2, "bob", object()]
# for item in list_of_things:
#     print("This is an item:", item)
