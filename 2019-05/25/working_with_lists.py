"""Working with Python lists exercise"""

# Let's create a list of names
names = ["James","Bob","Alice","John"]

# Now, get the length of the list"

length = len(names)

print("The length of the list is %d" % length)

# Let's create a new list with all of the names in upper case

upper_case_names = []

for name in names:
	upper_case_names.append(name.upper())
	
# Let's look at the documentation for the `list.sort()` method
print(list.sort.__doc__)

# Sort the list *in place*
upper_case_names.sort()

# Remove an item from the list by its index
upper_case_names.pop(0)

# Remove an item from the list by its value 
upper_case_names.remove("BOB")

# Append an item to the *end* of a list
upper_case_names.append("DIEGO")

# Insert an item at a specific position inside the list
upper_case_names.insert(2,"DMITRIY")
