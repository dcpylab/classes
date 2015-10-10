#!/usr/bin/env python
#-*-coding: utf-8-*-
#
# Simple bilingual dictionary that will let us translate
# holiday cards into Turkish
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

# from lookup import translate_phrase
import lookup

phrase = input("What phrase would you like to translate? ")
translated_phrase = lookup.translate_phrase(phrase)
print("English:", phrase)
print("Turkish:", translated_phrase)
