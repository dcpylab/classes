from __future__ import print_function

try:
	input = raw_input
except NameError:
	pass
	
	
def say_hello(name):

	a = "Other variable"
	
	print("Hello " + name)
	
name = input("What is your name? ")

say_hello(name)
	