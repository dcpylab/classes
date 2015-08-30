#!/usr/bin/env python
#
# Toy program to convert from Fahrenheit to
# Celsius!
#
from __future__ import print_function

table = {
    86: 30,
    79: 25,
    68: 20
}

def convert(f):
    return (f - 32) / 1.8

print("Convert from Fahrenheit to Celsius!")
fahrenheit = input("Temperature in F? ")
print("It's", fahrenheit, "F!")

fahrenheit = float(fahrenheit)
celsius = convert(fahrenheit)
round_celsius = round(celsius)
print("That means", round_celsius, "C!")

print("Some pro tips:")
for temp_f in table:
    temp_c = table[temp_f]
    print(temp_f, "in F is", temp_c, "in C")

print("Average time!")
total = 0
num_items = len(table)
for temp_f in table:
    total = total + temp_f
print("Average is:", total / num_items)
