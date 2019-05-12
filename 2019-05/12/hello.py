
def say_hello(name):
	"""
	Accepts one argument that's a string.
	Returns a string saying hello to `name`.
	"""
	# Using string interpolation
	return "Hello %s!" % name
	
	# Using string concatenation
	# return "Hello " + name + "!"
	
result = say_hello("Dmitriy")

print(result)

# For python2 users
# print result
