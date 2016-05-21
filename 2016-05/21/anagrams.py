#!/usr/bin/env python
#
# Write a program to find an anagram for a given word
# in a list of words. For bonus points, we'll read the
# word from user input, and the list of words from a file.
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass


def get_count_dictionary(word):
    counts = {}
    for letter in word:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] = counts[letter] + 1
    return counts


def is_equal(w1, w2):
    keys_in_w1 = w1.keys()
    keys_in_w2 = w2.keys()

    keys_in_w1 = sorted(keys_in_w1)
    keys_in_w2 = sorted(keys_in_w2)

    if keys_in_w1 != keys_in_w2:
        return False

    for k in w1:
        if w1[k] != w2[k]:
            return False

    return True


def find_anagrams(word, wordlist):
    anagrams = []
    target_counts = get_count_dictionary(word)
    for w in wordlist:
        word_counts = get_count_dictionary(w)
        if is_equal(word_counts, target_counts):
            anagrams.append(w)
    return anagrams

# instead of hard-coding 'team', we read from user input
target = input('What word should we look for? ')
# now we read our word list from a file
with open('./words.txt', 'r') as word_list:
    words = [w.strip() for w in word_list.readlines()]
    words = []
    for w in word_list.readlines():
        new_word = w.strip()
        words.append(new_word)

anagrams = find_anagrams(target, words)
print('We found:', anagrams)
