#!/usr/bin/env python
from __future__ import print_function
import time
from speeding import caught_speeding

start_time = time.time()
print("Yikes! You got stopped by a police officer!")
print("The officer says: do you know how fast you were going? ")
# PYTHON 2: raw_input("I was going: ")
speed_input = input("I was going: ")
speed = float(speed_input)
print("You get a ticket for speeding: %.2f" % caught_speeding(speed))
end_time = time.time()
print("This took:", end_time - start_time)
