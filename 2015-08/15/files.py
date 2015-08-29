#!/usr/bin/env python
#-*-coding: utf-8-*-
#
# Rosalind Intro problem:
#  Print all even-numbered lines from 'poem.txt', assuming 1-based
#  numbering of lines
#
from __future__ import print_function

poem_file = open("poem.txt", "r")
new_poem_file = open("poem2.txt", "w")

for index, line in enumerate(poem_file):
    line_number = index + 1
    if (line_number % 2 == 0):
        new_poem_file.write(line)
