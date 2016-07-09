'''
Example file of using python to control a turtle

Documentation for turtle
https://docs.python.org/2/library/turtle.html#module-turtle
'''
import turtle

james = turtle.Turtle()
james.shape("turtle")
james.color("red", 'green')

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("black", 'yellow')

# james.speed(2)
#


def spiral_star(turt):
    moves = 15
    colors = ['blue', 'orange']

    for move_number in range(moves):
        turt.forward(10 * move_number)
        turt.right(144)

        remainder = move_number % 2
        drawing_color = colors[remainder]
        turt.pencolor(drawing_color)

spiral_star(james)

bob.forward(100)
bob.right(144)

spiral_star(bob)


turtle.done()
