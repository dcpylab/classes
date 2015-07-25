#!/usr/bin/env python
#
# Calculate how much of a ticket to give you when you're
# caught speeding!
#

SPEED = 51

def caught_speeding(speed):
    """
    Calculate the ticket resulting from being caught speeding
    at the given speed.
    :param: speed Speed at which you were caught, as an integer
    :return: Integer describing the type of ticket: 0 = no ticket,
        1 = small ticket, 2 = big ticket
    """
    if speed <= 60:
        return 0
    elif speed > 60 and speed < 61:
        return "Write to the authorities, you've found a loophole"
    elif speed <= 80:
        return 1
    else:
        return 2
