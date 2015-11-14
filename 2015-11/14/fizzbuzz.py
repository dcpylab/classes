#!/usr/bin/env python
# Simple FizzBuzz program, prints the numbers from 1 to 100,
# with "fizz" for multiples of 3, and "buzz" for multiples of
# 5.
from __future__ import print_function

def generate_fizz_buzz(limit):
    i = 0
    while i < limit:
        if (i % 3) == 0 and (i % 5) == 0:
            yield "FizzBuzz"
        elif (i % 3) == 0:
            yield "Fizz"
        elif (i % 5) == 0:
            yield "Buzz"
        else:
            yield i
        # increase the value of i
        i += 1
    return

# call this function to kick it off
fizzbuzzer = generate_fizz_buzz(100)
for output in fizzbuzzer:
    print(output)

def dance_fizz_buzz(i, peanut_butter=100):
    if (i % 3) == 0 and (i % 5) == 0:
        print(i, "FizzBuzz")
    elif (i % 3) == 0:
        print(i, "Fizz")
    elif (i % 5) == 0:
        print(i, "Buzz")
    else:
        print(i)

    if i < peanut_butter:
        print_fizz_buzz(i + 1)


# Call the function to kick things off
#dance_fizz_buzz(1)

# for i in range(1, 101):
#     if (i % 3) == 0 and (i % 5) == 0:
#         print(i, "FizzBuzz")
#     elif (i % 3) == 0:
#         print(i, "Fizz")
#     elif (i % 5) == 0:
#         print(i, "Buzz")
#     else:
#         print(i)
