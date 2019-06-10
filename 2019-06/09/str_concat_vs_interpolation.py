
# Constants that we'll use to populate string fields
event = "DC Python"
location = "Eastern Market"
times = 4
name = "Dmitriy"

# String interpolation where you want to take into account the data type
filled_template_percent = "Welcome to %s at %s, %s. This is your %dth time attending." % (
	event,
	location,
	name,
	times
)

# String interpolation where the data type does not matter
filled_template_braces = "Welcome to {} at {}, {}. This is your {}th time attending.".format(
	event,
	location,
	name,
	times
)

# String *concatenation*; type converstion ("type casting") becomes necessary
filled_template_concat = "Welcome to " \
	+ event + " at " + location + ", " \
	+ name + ". This is your " + str(times) \
	+ "th time attending."
	
# All results come out the same
filled_template_percent == filled_template_braces
filled_template_percent == filled_template_concat
filled_template_braces == filled_template_concat
