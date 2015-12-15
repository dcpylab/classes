#!/usr/bin/env python
"""
Password Generator

Write a password generator in Python. Be creative with how you
generate passwords - strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols. The passwords should be random,
 generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

import random

# stolen from https://raw.githubusercontent.com/sindresorhus/word-list/master/words.txt
with open("words.txt", "r") as word_file:
    wordlist = [line.rstrip() for line in word_file]
    # the above list comprehension is equivalent to:
    # wordlist = []
    # for line in word_file:
    #     wordlist.append(line.rstrip())


def make_password(num_characters=8):
    password = random.choice(wordlist)
    while len(password) < num_characters:
        password += "-" + random.choice(wordlist)

    right_length_password = password[:num_characters]
    return right_length_password # .replace("\n", "_")


def main():
    print("Hello and welcome to the password generator!")
    num_characters = input("How long should it be? ")
    print("You asked for", num_characters, "in your password")
    int_num_characters = int(num_characters)
    new_password = make_password(int_num_characters)
    print("Your new password is:", new_password)


if __name__ == "__main__":
    main()
