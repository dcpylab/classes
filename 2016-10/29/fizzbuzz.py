"""
simple script for "FizzBuzz"; i.e. printing the
integers from 1 to 100, but printing "fizz" for
multiples of 3, "buzz" for multiples of 5, and
"fizzbuzz" for multiples of both
"""
from __future__ import print_function
import sys
try:
    input = raw_input
except NameError:
    pass

print("Welcome to FizzBuzz!")

def is_multiple_of(i, n):
    remainder = i % n
    result = (remainder == 0)
    return result



target_string = input("Enter maximum number for FizzBuzz: ")
try:
    target = int(target_string)
except ValueError:
    print(target_string, "is not a number. Please try again.")
    sys.exit(1)

integers = range(1, target + 1)
for i in integers:
    if is_multiple_of(i, 3) and is_multiple_of(i, 5):
        print("fizzbuzz")
    elif is_multiple_of(i, 3):
        print("fizz")
    elif is_multiple_of(i, 5):
        print("buzz")
    else:
        print(i)

print("I guess we're done with FizzBuzz!")
