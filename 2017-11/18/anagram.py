from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

def words_match(w1, w2):
    if w1 == w2:
        return True
    else:
        return False

known_words = [
    "apple",
    "banana",
    "carrot",
    "donut",
    "shoes",
    "smile",
]

word = input("Type a word here: ")

found = False
for w in known_words:
    if words_match(w, word):
        found = True
        print("  Hey! the words are equal!", w, word)

if found:
    print("COngrats!")
else:
    print("Bad luck")
