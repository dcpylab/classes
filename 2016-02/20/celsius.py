#
# Simple Celsius to Fahrenheit converter
#   user inputs a temperature in Celsius,
#   and it outputs the corresponding
#   Fahrenheit
#
from __future__ import print_function
try:
    input = raw_input
except NameError:
    pass

def convert_to_fahrenheit(degrees):
    """Convert the given degrees Celsius
    into Fahrenheit, and return it."""
    result = degrees * (9.0 / 5.0) + 32
    return result

user_degrees = input("Temp in Celsius: ")
CELSIUS = float(user_degrees)

FAHRENHEIT = convert_to_fahrenheit(CELSIUS)

print("Well", CELSIUS, "degrees in Celsius is:",
      FAHRENHEIT, "degrees in Fahrenheit!")
