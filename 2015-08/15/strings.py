#!/usr/bin/env python
#-*-coding: utf-8-*-
#
# Rosalind Intro problem:
#  Given a string and four integers a, b, c, d -- print slices of the
#  string from indices a through b, c through d
#
from __future__ import print_function

a_string = "hello"

sample_string = """HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."""

a = 22
b = 27
c = 97
d = 102

slice1 = sample_string[a:b + 1]
print(slice1)
slice2 = sample_string[c:d + 1]
print(slice2)
