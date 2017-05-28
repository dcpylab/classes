#
# Simple script to find anagrams
# for a given word in a list.
#
import sys
from itertools import permutations

target = "steamroller"
words = [
    "meats", "empire", "python",
    "fallout", "word", "palace",
    "maets", "meatrsoller"
    ]

def sort_word(word):
    return sorted(word)

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    sorted1 = sort_word(word1)
    sorted2 = sort_word(word2)
    return sorted1 == sorted2

def anagrams(word, list_of_words):
    results = []
    for w in list_of_words:
        if is_anagram(w, word):
            results.append(w)
    return results

found_anagrams = anagrams(target, words)
print(found_anagrams)
