#
# simple program to translate words in one language into
# words in another, for use in translating Christmas cards
#
try:
    input = raw_input
except NameError:
    pass

translations = {
    "merry": "errymay",
    "christmas": "istmaschray",
    "happy": "appyhay",
    "new": "ewnay",
    "year": "earyay",
}

def translate_word(word):
    t = translations.get(word, '[unknown]')
    return t

def translate_phrase(phrase):
    words = phrase.split()
    translated = []
    for w in words:
        translated_word = translate_word(w)
        translated.append(translated_word)

    separator = " "
    translated_phrase = separator.join(translated)
    return translated_phrase

greeting = input("what is your phrase? ")
print(greeting)
print("translates to:")
translated_greeting = translate_phrase(greeting)
print(translated_greeting)
