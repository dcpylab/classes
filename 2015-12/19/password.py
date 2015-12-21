#!/usr/bin/env python
#
# Password generator: let the user enter a
# length of password they would like, and
# generate for them a password of that length,
# randomly
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

import string
import random

pool = (string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation)


def generate_password(num_of_chars):
    """Randomly generate a password!"""
    password = ""

    while len(password) < num_of_chars:
        random_character = random.choice(pool)
        password += random_character

    return password


if __name__ == "__main__":
    raw_num_of_chars = input("How long should the password be? ")
    num_of_chars = int(raw_num_of_chars)
    print("You asked for", num_of_chars, "characters in your password")

    password = generate_password(num_of_chars)

    print("Your password is:", password)
