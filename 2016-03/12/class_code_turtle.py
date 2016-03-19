#!/usr/bin/python3
"Classroom example using turtle to learning more about python programming  "

import turtle

wn = turtle.Screen()
# wn.bgcolor('black')
wn.title('The Sandbox')
wn.setup(500,500)
wn.colormode(255)

george = turtle.Turtle()

george.shape('turtle')


# make a rectangle 
# and make george go back where he started

george.forward(100)
george.left(90)
george.forward(50)
george.left(90)
george.forward(100)
george.left(90)
george.forward(50)

wn.mainloop()

# make a triangle
# make george go back to where he started
# george.left(180)

# george.forward(200)
# george.left(120)
# george.forward(200)
# george.left(120)
# george.forward(200)

# make a triangle with a different color on each side
# use a  for-loop

# colors = ['red', 'yellow', 'blue']

# for color in colors:
#     # do something
#     george.color(color)
#     george.forward(200)
#     george.left(120)

### write a function that draws a triangle with just one color

# def draw_triangle(draw_color):
#     # do something here
#     # a triangle has three sides ### Hint for-loop
#     for side in range(3):
#         george.color(draw_color)
#         george.forward(200)
#         george.left(120)

# draw_triangle('green')

# george.penup()

# george.right(45)

# george.pendown()

# draw_triangle('red')

# import random

# def snowflake_screen(num_iterations):   
#     george.speed(speed=0)
#     for n in range(num_iterations):
#         george.pencolor(random.randrange(256),random.randrange(256),random.randrange(256))
#         for side in range(3):
#             george.forward(150)
#             george.left(120)
#         george.left(random.randrange(25))
#         george.forward(5)

# snowflake_screen(100)



print('hello, everything works so far! I think....')





