#!/usr/bin/env python
#-*-coding: utf-8-*-
"""
DNA is composed of four bases - adenine, thymine, cytosine, guanine - paired as follows: A-T and G-C.

Meaning: on one side of the strand there may be a series of bases

A T A A G C

And on the other strand there will have to be

T A T T C G

It is your job to generate one side of the DNA strand and output the two DNA strands. Your program should take a DNA sequence as input and return the complementary strand.
Input

A A T G C C T A T G G C
Output

A A T G C C T A T G G C
T T A C G G A T A C C G
"""
from __future__ import print_function
import sys
if sys.version_info[0] == 2:
    input = raw_input

"""
Goal: Create a complementary DNA strand from an input strand
DNA bases pair up as G-C, A-T
"""

# input_strand = input("Enter DNA here: ")

# Here we load the data from a file
filename = input("Enter file name here: ")

# input_file = open(filename, "r")
# input_strand = input_file.read()
# input_file.close()
with open(filename, "r") as input_file:
    input_strand = input_file.read()

# Clean up the input strand
input_strand = input_strand.strip()
input_strand = input_strand.upper()

translation_table = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
    " ": " "
}
# output_strand = input_strand.translate(translation_table)

output_strand = ""
for base in input_strand:
    if base in translation_table:
        complement = translation_table[base]
        # same as: output_strand = output_strand + complement
        output_strand += complement
    else:
        print("Uh-oh, I do not recognize the input: ", base)
        sys.exit(1)

print(input_strand)
print(output_strand)
