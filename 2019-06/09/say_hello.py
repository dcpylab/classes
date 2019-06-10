
def say_hello(name):
	return "Welcome to DC Python, %s" % name

# Use `raw_input` instead of `input` for Python 2
# name = raw_input("What is your name? ")

name = input("What is your name? ")

print(say_hello(name))
