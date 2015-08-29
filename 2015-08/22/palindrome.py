#!/usr/bin/env python
"""
Write a version of a palindrome recognizer that also accepts
phrase palindromes such as ""Go hang a salami I'm a lasagna hog."", ""Was
it a rat I saw?"", ""Step on no pets"", ""Sit on a potato pan, Otis"", ""Lisa
Bonet  ate no basil"", ""Satan, oscillate my metallic sonatas"", ""I roamed
under it as a tired nude Maori"", ""Rise to vote sir"", or the exclamation
""Dammit, I'm mad!"". Note that punctuation, capitalization, and spacing
are usually ignored.
"""
from __future__ import print_function

test_palindromes = [
    "Go hang a salami I'm a lasagna hog.",
    "Was it a rat I saw?",
    "Step on no pets",
    "Sit on a potato pan, Otis",
    "Lisa Bonet ate no basil",
    "Satan, oscillate my metallic sonatas",
    "I roamed under it as a tired nude Maori",
    "Rise to vote sir",
    "Dammit, I'm mad!",
    # These are *not* palindromes! They should be rejected!
    "Rolls-Royce is a cool type of car",
    "It's a beautiful day today",
    "A Lamborghini is nicer than a Rolls, says Q"
]

def is_palindrome(phrase):
    translation_table = {
        " ": "",
        "'": "",
        ".": "",
        "!": "",
        "?": "",
        "-": "",
        '"': "",
        ",": "",
    }
    for item in translation_table.items():
        character = item[0]
        replacement = item[1]
        phrase = phrase.replace(character, replacement)
    phrase = phrase.lower()
    reversed_phrase = phrase[::-1]
    if phrase == reversed_phrase:
        return True
    else:
        return False

for phrase in test_palindromes:
    is_it_palindrome = is_palindrome(phrase)
    print(phrase, is_it_palindrome)
    # this is in the loop

headers = set()
results = []
for row in DictReader():
    xml_data = dict(flatten_dict(parsing_magic()))
    row.update(xml_data)
    results.append(row)
    headers.update(row.keys())

# after the loop, headers is the union of all sets of keys
headers_list = list(headers)
write_to_csv(headers_list)
for row in results:
    data = [row.get(x, '') for x in headers_list]
    write_row(data)
