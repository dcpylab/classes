"""
simple script for "FizzBuzz"; i.e. printing the
integers from 1 to 100, but printing "fizz" for
multiples of 3, "buzz" for multiples of 5, and
"fizzbuzz" for multiples of both
"""
import functools
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

is_multiple_of_three = functools.partial(is_multiple_of, n=3)
is_multiple_of_five = functools.partial(is_multiple_of, n=5)
is_multiple_of_seven = functools.partial(is_multiple_of, n=7)

conditions = [
    (is_multiple_of_three, "fizz"),
    (is_multiple_of_five, "buzz"),
    (is_multiple_of_seven, "bazz"),
]

target_string = input("Enter maximum number for FizzBuzz: ")
try:
    target = int(target_string)
except ValueError:
    print(target_string, "is not a number. Please try again.")
    sys.exit(1)

integers = range(1, target + 1)
for i in integers:
    output = ""
    for cond, string in conditions:
        if cond(i):
            output += string
    if output:
        print(output)
    else:
        print(i)

print("I guess we're done with FizzBuzz!")
