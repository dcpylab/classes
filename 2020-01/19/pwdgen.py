import string
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('length', type=int, help='How long?')
parser.add_argument('--upper', action='store_true')
parser.add_argument('--lower', action='store_true')

args = parser.parse_args()

length = args.length
use_upper = args.upper
use_lower = args.lower

# print(string.ascii_uppercase)
# print(string.ascii_lowercase)

characters = ''

if use_upper:
    characters += string.ascii_uppercase

if use_lower:
    characters += string.ascii_lowercase

password = ''
for i in range(length):
    password += random.choice(characters)

print(password)


