#!/usr/bin/env python
#-*-coding: utf-8-*-
#
# Simple program to input a list of children and
# sort them by age
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

# We can represent a child as a dictionary, with "name" and "age" fields
child1 = {
    "name": "John",
    "age": 20
}
child2 = {
    "name": "Rami",
    "age": 30
}

# Let's get all the children's names
names = input("What are the names of your children? (Please separate with spaces) ")
names = names.split(" ")
print(names)

# Let's get all their ages
ages = input("What are the ages of your children? (Please separate with spaces) ")
ages = ages.split(" ")
print(ages)

# Since each list is in order, we know that they line up, e.g.
# the first entry in `names` matches up with the first entry in
# `ages`, to give us the details for the first child. The same is
# true for second, third, etc entries in both lists. So we are now
# going through and creating a dictionary to represent each child.
number_of_children = len(names)
children = []
for i in range(number_of_children):
    name = names[i]
    age = ages[i]
    child = {
        "name": name,
        "age": age
    }
    children.append(child)

# Now we have a list of children -- we can sort them by age

# Define a helper function to extract the age for each child
def get_age(child):
    return child["age"]

# Sort the children using the `get_age` function to find the
# "sort key" to use -- and we're done!
sorted_children = sorted(children, key=get_age)
print(sorted_children)

## Notes on how Python does this kind of sorting
# The algorithm is called "decorate-sort-undecorate"

# We start out with a list of things we want sorted -- this can
# be a list of any kind of item
list_of_things = ["Coke", "Fanta", "Pepsi", "Dr Pepper"]

# We "decorate" the list of things by using `value_function` to
# find the value we want to use for the sorting, and create a
# tuple with that value as the first item and our thing as the second
decorated_list_of_things = []
for thing in list_of_things:
    decorate_value = value_function(thing)
    decorated_thing = (decorate_value, thing)
    decorated_list_of_things.append(decorated_thing)

# We can then use Python's built-in sort to sort it, since
# Python will sort tuples by their first item -- and the first
# item in each tuple is the sort value we want
sorted_decorated_list = sorted(decorated_list_of_things)

# Now we remove the sort values and restore our original list
# structure
sorted_list_of_things = []
for value_and_thing in sorted_decorated_list:
    thing = value_and_thing[1]
    sorted_list_of_things.append(thing)
