import random
import string
try:
    input = raw_input
except NameError:
    pass


def ask_user(type_):
    result = input('use ' + type_ + '? ')
    return result.lower().startswith('y')


pool_lowercase = string.ascii_lowercase
pool_uppercase = string.ascii_uppercase
pool_digits = string.digits
pool_special = '!@#$%^&*()_-+=~[]{}|<>?/\\'

pool = ''

pool_types = [k for k in globals() if k.startswith('pool_')]
for var in pool_types:
    pool_type = var[len('pool_'):]
    should_use = ask_user(pool_type)
    if should_use:
        pool += globals()[var]

print('This is your pool:', pool)

password_length = input('length? ')
int_password_length = int(password_length)

password = ''
for i in range(int_password_length):
    password += random.choice(pool)

print('Huzzah! A password!\n\t', password)
