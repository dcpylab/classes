#!/usr/bin/env python
#
# Simple password generator: type in a length of password you
# want and it gives you a random new password of that length.
#
from __future__ import print_function
import string
import random

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numeric = string.digits

pool = lowercase + uppercase + numeric

raw_password_length = input("How long should it be? ")
password_length = int(raw_password_length)
numbers_up_to_password_length = range(password_length)
password_string = ''
for i in numbers_up_to_password_length:
    random_character = random.choice(pool)
    password_string = password_string + random_character

print("Your random password:", password_string)
