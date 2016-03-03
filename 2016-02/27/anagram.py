#!/usr/bin/env python3
#
# Anagram finder -- find anagrams for a given word
# in a list of words
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

from collections import Counter


def count_letters(word):
    """Return a dictionary counting the letters
    in the given word."""
    counts = {}
    for letter in word:
        count = 1
        if letter in counts:
            count = counts[letter] + 1
        counts[letter] = count
    return counts


def is_anagram(a, b):
    """Are strings `a` and `b` anagrams of each other?
    Returns whether they are or not."""
    if len(a) != len(b):
        return False

    letters_in_a = Counter(a)
    letters_in_b = Counter(b)
    are_they_equal = (letters_in_a == letters_in_b)
    return are_they_equal


if __name__ == '__main__':
    target = input("What is your target word? ")
    word_list = [
        "happy",
        "sad",
        "rhino",
        "rosceonirh", # fake anagram
        "scenirho", # all the same letters
        "scenirhooo"
    ]

    print("Finding anagrams for:", target, "...")
    found_anagrams = []
    for word in word_list:
        is_word_an_anagram = is_anagram(word, target)
        if is_word_an_anagram:
            found_anagrams.append(word)

    print("found:", found_anagrams)
