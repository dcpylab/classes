#
# Represent a small bilingual lexicon in Python and use it to
# translate your Christmas cards from English into French. That is,
# write code that takes a list of English words and returns a list of
# French words.
#
try:
    input = raw_input
except NameError:
    pass

translation = {}
translation["Happy"] = "Joyeux"
translation["New"] = "Nouvelle"
translation["Year"] = "Annee"


def translate(word):
    """Given an English word, return the equivalent
    French word."""
    return translation[word]


input_from_user = input("What should the card say?")
words_in_user_input = input_from_user.split(" ")

output_words = []
for word in words_in_user_input:
    translated_word = translate(word)
    output_words.append(translated_word)

output_phrase = " ".join(output_words)
print(output_phrase)
