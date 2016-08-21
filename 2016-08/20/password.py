#
# Simple password generator. Creates a password of a given
# length randomly.
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

import string
import random


length = input('How many characters in the password? ')
int_length = int(length)
print('You want a password of', length, 'characters')
include_punctuation = input('Do you want punctuation? Y/N ')
pool = string.ascii_lowercase + string.ascii_uppercase +\
       string.digits

if include_punctuation == 'Y':
    pool = pool + string.punctuation

print('You are using a pool of characters:', pool)

password = ''
for i in range(int_length):
    random_character = random.choice(pool)
    print("  We randomly picked:", random_character)
    password = password + random_character
    print("  The value of password is now:", password)

print("Now your password is:", password)
