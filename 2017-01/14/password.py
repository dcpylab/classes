import random
import string
try:
    input = raw_input
except NameError:
    pass

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = '!@#$%^&*()_-+=~[]{}|<>?/\\'

pool = ''

use_lowercase = input('use lowercase? ')
if use_lowercase == 'y':
    pool += lowercase

use_uppercase = input('use uppercase? ')
if use_uppercase == 'y':
    pool += uppercase

use_digits = input('use digits? ')
if use_digits == 'y':
    pool += digits

use_special = input('use special? ')
if use_special == 'y':
    pool += special

print('This is your pool:', pool)

password_length = input('length? ')
int_password_length = int(password_length)

password = ''
for i in range(int_password_length):
    password += random.choice(pool)

print('Huzzah! A password!\n\t', password)
