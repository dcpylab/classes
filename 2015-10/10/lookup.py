#-*-coding: utf-8-*-
# we need to translate the words:
# merry, christmas, happy, new, year
dictionary = {
    "merry": "mutlu",
    "happy": "mutlu",
    "christmas": "noel",
    "new": "yeni",
    "year": "yıl"
}

def translate_phrase(phrase):
    lowercase_phrase = phrase.lower()
    words = lowercase_phrase.split(" ")
    turkish_words = []
    for word in words:
        turkish_word = dictionary[word]
        turkish_words.append(turkish_word)

    turkish_phrase = " ".join(turkish_words)
    turkish_phrase = turkish_phrase.title()
    return turkish_phrase
