import os

# print "hello"  # python2
# print("hello") # python3

name = "Dmitriy"
# print(name)

cwd = os.getcwd()
# print(cwd)


def say_hello(name):

	template = "Hello %s, welcome to DC Python!"
	result = template % name

	return result

def say_hello_event(name, event):

	template = "Hello %s, welcome to %s!"
	result = template % (name, event)

	return result

# name = raw_input("What is your name? ")

name = input("What is your name? ")
event = input("What event are you attending? ")

output = say_hello_event(name, event)

print(output)


"""

(1) Anagrammatic - 7
(2) Aviation Code - 8
(3) FizzBuzz - 7

"""





