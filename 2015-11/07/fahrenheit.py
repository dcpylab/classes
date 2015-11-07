#!/usr/bin/env python
#
# A simple program to convert an input temperature
# in Fahrenheit into one in Celsius
#
# NOTE: this makes `print` work the same in Python 2 and 3
from __future__ import print_function
# NOTE: this makes `input` work the Python 3 way in Python 2
try:
    input = raw_input
except NameError:
    pass

import datetime
import calendar

temperature_ranges = {
    "January": (-5, 5),
    "November": (-5, 15)
}

input_temp = input("What is the temperature in Fahrenheit? ")
print("The user typed:", input_temp)
fahrenheit = int(input_temp)
celsius = (fahrenheit - 32) / 1.8

now = datetime.datetime.now()
month_name = calendar.month_name[now.month]
print("Python thinks it is the month of:", month_name)
temp_range = temperature_ranges[month_name]
print("The range of temperatures is:", temp_range)

lowest, highest = temp_range
if lowest <= celsius <= highest:
    print("It is normal for this time of year")
elif celsius < lowest:
    print("It's unseasonably cold!")
elif celsius > highest:
    print("It's rather warm!")
else:
    print("I'm mathematically impossible!")


output_template = "Fahrenheit: {FH:.2f} = Celsius: {CL:.2f}"
output = output_template.format(FH=fahrenheit, CL=celsius)
print(output)
