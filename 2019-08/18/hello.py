
def say_hello(name):
	""" Example with percent formatting """
	template = "Hello %s!"
	filled = template % name
	return filled

# print("Hey!")

"""
Some description here.
print("Hey!")
"""

def say_hello_format(name):
	""" 
	Function that says hello to `name`.
	"""
	
	template = "Hello {}!"
	filled = template.format(name)
	
	return filled

def say_hello_concat(name):
	""" Example of str concatenation """
	return "Hello " + name + "!"

# For python2 it's `raw_input`
name = input("What is your name? ")

statement = say_hello(name)

# For python2 `print statement`
print(statement)

"""
Voting

- Basic stats - 8
- Anagrams - 0
- Pwd gen - 9
- NATO - 0
- FizzBuzz - 2



"""





	