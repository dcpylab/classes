#!/usr/bin/env python
#
# be creative with how you generate passwords -- strong
# passwords have a mixture of uppercase and lowercase
# letters, numbers, and special characters
# passwords should be random, and we should generate a new
# one every time the user asks.
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    # NOTE: This error will be thrown on Python 3,
    # where `raw_input` is not defined. If that's the
    # case, then the function we're looking for is already
    # in place, so we don't do anything and continue as
    # normal.
    pass

import random
import string

num_of_chars = input("How many characters should the password be? ")
num_of_chars = int(num_of_chars)
print("The user said:", num_of_chars)

pool_of_characters = string.ascii_letters + string.digits + string.punctuation
size_of_pool = len(pool_of_characters)

password = ""
for i in range(0, num_of_chars):
    random_index = random.randint(0, size_of_pool)
    random_char = pool_of_characters[random_index]
    password += random_char

print("I've generated:", password)
