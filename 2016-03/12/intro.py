'''
Demo of turtle- stolen from:

http://interactivepython.org/runestone/static/thinkcspy/index.html
'''

import turtle
import random

def main():
    wn = turtle.Screen()
    wn.setup(1000,1000)
    wn.colormode(255)
    tList = []
    head = 0
    numTurtles = 10
    for i in range(numTurtles):
        nt = turtle.Turtle()   # Make a new turtle, initialize values
        nt.setheading(head)
        nt.pensize(2)
        nt.pencolor(random.randrange(256),random.randrange(256),random.randrange(256))
        nt.speed(10)
        wn.tracer(30,0)
        tList.append(nt)       # Add the new turtle to the list
        head = head + 360/numTurtles

    for i in range(100):
        moveTurtles(tList,15,i)

    w = tList[0]
    w.up()
    w.goto(0,40)
    w.write("Welcome to the",True,"center","80pt")
    w.goto(0,-35)
    w.write("Python Lab",True,"center","80pt")
    wn.mainloop()  

def moveTurtles(turtleList,dist,angle):
    for turtle in turtleList:   # Make every turtle on the list do the same actions.
        turtle.forward(dist)
        turtle.right(angle)

main()