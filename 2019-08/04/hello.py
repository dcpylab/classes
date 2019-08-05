

def introduction_percent(name, event, nattended):
	""" Provides an introduction to attendant using percent formatting. """
	template = "Hello %s, welcome to %s! This is your %dth time attending."
	statement = template % (name, event, nattended)
	
	return statement
	
def introduction_format(name, event, nattended):
	""" Provides an introduction to attendant using `format` method. """
	template = "Hello {}, welcome to {}! This is your {}th time attending."
	statement = template.format(name, event, nattended)
	
	return statement
	
def introduction_concat(name, event, nattended):
	""" Provides an introduction to attendant using string concatenation. """
	statement = "Hello " + name + ", welcome to " + event + "! This is your " + str(nattended) + "th time attending."
	
	return statement
	
# In Python 2 will be `raw_input`
name = input("What is your name? ")
event = input("What event are you attending? ")
ntimes = input("How many times have you attended? ")

# statement = introduction_percent(name, event, int(ntimes))
# statement = introduction_format(name, event, int(ntimes))
statement = introduction_concat(name, event, int(ntimes))

print(statement)

"""

Voting 

1. WMATA API - 7 (9)
2. Advent of Code - 3
3. Gapminder Stats - 9 (7)
4. Anagrammatic - 1

"""




