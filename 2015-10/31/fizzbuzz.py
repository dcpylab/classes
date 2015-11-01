#!/usr/bin/env python
#
# toy program to execute FizzBuzz, i.e.
# print integers from 1 to 100, for multiples of 3
# print "fizz", for multiples of 5 print "buzz",
# and "fizzbuzz" for multiples of both
#
from __future__ import print_function

def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 or i % 5 == 0):
            print("FizzBuzz", i)
        elif i % 3 == 0:
            print("Fazz", i)
        elif i % 5 == 0:
            print("Bazz", i)
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz()
