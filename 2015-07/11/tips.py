#!/usr/bin/env python
#
# Toy program to calculate tip for a restaurant visit
#
from __future__ import print_function
from calculations import calculate_tip
from math import ceil
from random

# Python 2
# bill = raw_input("What was the bill? ")
# percent = raw_input("How much do you want to tip? ")
# Python 3
bill = input("What was the bill? ")
percent = input("How much do you want to tip? ")

bill = float(bill)
percent = float(percent)

tip = calculate_tip(bill, percent)
total = bill + tip
rounded_total = ceil(total)

print("Your bill was:", bill)
print("You're tipping:", percent)
print("Your total is:", rounded_total)
