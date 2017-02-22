"""
Introduction to Python
DATE - 18 February 2017
Instructor - Nathan Danielsen @nate_somewhere
https://github.com/ndanielsen/beginning-python/
"""

"""
Exercise 1:

From the following header extract:
1. Extract the title
2. Extract the introduction
3. Extract the author
4. Extract the photographer

*Hint*: Google something called repr and check what `print(repr(header))` tells you.

Note: For a guided, step by step solution in jupyter notebooks go to:
https://github.com/ncclementi/dcpython_exercises/blob/master/02-18-17_application_real_data.ipynb
"""

header = """
    My President Was Black
    A history of the first African American White House—and of what came next

    By Ta-Nehisi Coates
    Photograph by Ian Allen
    """

#Using the hint:
#Uncomment the following line to see the output of repr(header)

#print(repr(header))

#Splitting and saving to a list.
header_list = header.split('\n')

#Removing extra white spaces in each element of our list.
for i in range(len(header_list)):
    header_list[i] = header_list[i].strip()

#Removing empty ('') elements.
for element in header_list:
    if element == '':
        header_list.remove(element)

#Getting title and introduction.
title = header_list[0]
intro = header_list[1]

#Getting author and photographer.
#Here we strip out the part we don't want.
author = header_list[2].strip('By ')
photographer = header_list[3].strip('Photograph by ')

#Print information required
print('Title       : ', title)
print('Introduction: ', intro)
print('Author      : ', author)
print('Photographer: ', photographer)


