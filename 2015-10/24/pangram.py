#
# This is a simple program to decide whether or not an input
# sentence is a pangram, i.e. contains all the letters of the
# English alphabet.
#
# NOTE: The below code makes Python 2 `print` behave like Python 3
# `print`
from __future__ import print_function
# NOTE: The below code tries to rename the `input` function
# in Python 2 to work like Python 3. If there's an error, that
# means you're already using Python 3, so it's OK.
try:
    input = raw_input
except NameError:
    pass

import string

sentence = input("Please type a sentence: ")
lowercase_sentence = sentence.lower()
letters_in_sentence = set(lowercase_sentence)

alphabet = set(string.ascii_lowercase)

is_pangram = letters_in_sentence.issuperset(alphabet)

print("Is it a pangram?", is_pangram)

# alphabet = list(string.ascii_lowercase)

# lowercase_sentence = sentence.lower()
# letters_in_sentence = list(lowercase_sentence)

# is_pangram = True
# for letter in alphabet:
#     if letter in letters_in_sentence:
#         # Do nothing
#         pass
#     else:
#         is_pangram = False

# print("Is it a pangram?", is_pangram)
