import os

print(os.getcwd())

# print os.getcwd()

"""

Vote 

- FizzBuzz - 11
- NATO - 4
- PWD - 1
- Anagrams - 4


"""

def say_hello(name):
	"""
	Says hello to `name`.
	"""
    
	statement = "Hello %s, welcome to DC Python!" % name
	
	return statement
	
# result = say_hello("Dmitriy")
# print(result)

def say_hello_again(name, event):
    
	statement = "Hello {name}, welcome to {event}!".format(
		name=name,
		event=event
	)
	
	# statement = "Hello %s, welcome to %s!" % (
		# name,
		# event
	# )
	
	return statement

# Python 2 use `raw_input`
# name = raw_input("What is your name? ")
# event = raw_input("What are you attending? ")

name = input("What is your name? ")
event = input("What are you attending? ")

result = say_hello_again(name, event)

print(result)
