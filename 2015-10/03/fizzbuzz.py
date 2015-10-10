#
# FizzBuzz: print out the numbers from 1 to 100;
# for multiples of 3, print "Fizz", for multiples of 5
# print "Buzz", and for multiples of both print "FizzBuzz"
#
from __future__ import print_function
from multiples import *

# for i in range(1, 101):
#     if mult_of_3(i) and mult_of_5(i):
#         print("FizzBuzz")
#     elif mult_of_3(i):
#         print("Fizz")
#     elif mult_of_5(i):
#         print("Buzz")
#     else:
#         print(i)

def fizzbuzz(x):
    if mult_of_3(x) and mult_of_5(x):
        return "FizzBuzz"
    elif mult_of_3(x):
        return "Fizz"
    elif mult_of_5(x):
        return "Buzz"
    else:
        return str(x)

lines = [str(fizzbuzz(i)) for i in range(1, 101)]
separator = "\n"
collected_lines = separator.join(lines)

print(collected_lines)
