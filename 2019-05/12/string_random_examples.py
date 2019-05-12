import string
import random

print("Lower case ASCII letters: %s" % string.ascii_lowercase)
print("Upper case ASCII letters: %s" % string.ascii_uppercase)

print("Punctuation: %s" % string.punctuation)
print("Digits: %s" % string.digits)

# Convert a string to a list
lower_case_list = list(string.ascii_lowercase)

# Select a random element from a list
random_elm1 = random.choice(lower_case_list)
random_elm2 = random.choice(lower_case_list)

print("My random elements are '%s' and '%s'" % (random_elm1, random_elm2))

# Randomize the order of the list; notice that this randomization
# is performed "in place"; this is because lists are *dynamic* arrays,
# meaning that they are *mutable* and can be changed in place

random.shuffle(lower_case_list)

# Convert the list back to a string
lower_case_random = "".join(lower_case_list)

print("My randomized lower case string is %s" % lower_case_random)
