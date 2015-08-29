#!/usr/bin/env python
#-*-coding: utf-8-*-
#
# Rosalind Intro problem:
#  Given two integers a and b, where a < b < 1000, print the sum of
#  all odd integers between a and b
#
from __future__ import print_function

a = 100
b = 200

total = 0
for integer in range(a, b):
    remainder = integer % 2
    if remainder == 1: # number is odd
        total = total + integer

print("The total is:", total)

my_list = [2, 'Q', [], 347]

all_numbers = range(a, b)
only_odd_numbers = [x for x in all_numbers if x % 2 == 1]
total2 = sum(only_odd_numbers)
print("The total, another way:", total2)
print("yet another way:", sum([x for x in range(a, b) if x % 2]))
