#
# Simple script to generate passwords in Python
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

import random
import string


length = input("How long a password do you want? ")
length = int(length)
print("You wanted", length, "characters")

character_types = {
    'lowercase': False,
    'uppercase': False,
    'number': False,
    'special': False
}

for char_type in character_types:
    user_says = input(
        "Use {} [Y/N]? ".format(char_type))
    user_says_lower = user_says.lower()
    user_said_y = user_says_lower.startswith("y")
    character_types[char_type] = user_said_y

character_pools = {
    'uppercase': list(string.ascii_uppercase),
    'lowercase': list(string.ascii_lowercase),
    'number': list(string.digits),
    'special': list(string.punctuation)
}

pool = []
for char_type in character_types:
    if character_types[char_type]:
        pool.extend(character_pools[char_type])

password = ""
for i in range(length):
    password = password + random.choice(pool)

print(password)
