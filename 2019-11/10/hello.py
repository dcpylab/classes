
# snake case = say_hello
# camelCase = sayHello

def say_hello(name):
	"""
	Accepts a name str variable and returns populated statement.
	"""
	
	template = "Hello %s, welcome to DC Python!"
	statement = template % name
	
	return statement


# Python2 users will use `raw_input`
# Python2 users will use `print "string"`

name = input("What is your name? ")

result = say_hello(name)

print(result)

"""

AOC - 11
Annagrammatic - 3
Pwd generator - 12
Aviation Code - 2
FizzBuzz - 8


"""




