#
# Password Generator -- ask the user for a preferred length of password
# and then randomly generate a password of that length. Must contain upper
# case, lower case, and number characters.
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

import random
# Because I'm lazy and don't want to type out all the letters and numbers,
# I'm loading them in from Python's built-in `string` module. The below
# is the same as defining `pool_of_characters = 'abcd...'`
import string
pool_of_characters = string.ascii_lowercase + string.ascii_uppercase +\
                     string.digits + string.punctuation

def get_random_character():
    rand_char = random.choice(pool_of_characters)
    return rand_char

print("Hello! We'll be generating passwords today.")
desired_length_raw = input("How long should it be? ")
desired_length = int(desired_length_raw)
print("You asked for", desired_length, "characters in your password")

password = ""
for _ in range(desired_length):
    # do something that will add a random character to our password
    password = password + get_random_character()

print("Your new password is:", password)
