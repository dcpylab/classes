#!/usr/bin/env python
#-*-coding: utf-8-*-
#
# Rosalind Intro problem:
#  Given two numbers, print the sum of their squares
#
from __future__ import print_function
import math

number1 = 3
number2 = 5

number1_squared = number1 ** 2
number2_squared = number2 * number2

sum_of_squares = number1_squared + number2_squared
hypotenuse = sum_of_squares ** 0.5

print("Number1 is:", number1)
print("Number2 is:", number2)
print("The sum of their squares is:", sum_of_squares)
print("The hypotenuse is:", hypotenuse)
