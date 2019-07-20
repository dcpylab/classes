""" String formatting examples """

def say_hello_simple(name, ntimes, event):
	""" String interpolation -> https://pyformat.info/ """

	template = "Hello %s! This is your %dth time attending %s." 
	
	# No keyword arguments required
	template_filled = template % (
		name,
		ntimes,
		event
	)
	
	return template_filled

def say_hello_format(name, ntimes, event):
	""" Using the `.format()` method """

	template = "Hello {name}! This is your {ntimes}th time attending {event}." 
	
	# Keyword arguments needed
	template_filled = template.format(
		name=name,
		ntimes=ntimes,
		event=event
	)
	
	return template_filled

def say_hello_concat(name, ntimes, event):
	""" Using string concatenation """

	statement = "Hello " + name \
		+ "! This is your " \
		+ str(ntimes) \
		+ "th time attending " \
		+ event \
		+ "." 
	
	return statement

# For Python 2 users
# name = raw_input("What is your name? ")

# For Python 3 users
name = input("What is your name? ")
ntimes = input("How many times have you attended? ")
event = input("What event are you attending? ")

# All three will return the same string
statement_simple = say_hello_simple(name, int(ntimes), event)
statement_format = say_hello_format(name, int(ntimes), event)
statement_concat = say_hello_concat(name, int(ntimes), event)

# For Python 2 users
# print statement_simple

# For Python 3 users
print(statement_simple)
print(statement_format)
print(statement_concat)


"""

Votes

- Aviation Code = 14
- AOC = 11
- Anagrammatic = 2
- GOT = 2
- WMATA = 9

"""
