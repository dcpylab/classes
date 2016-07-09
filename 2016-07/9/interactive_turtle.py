"""
Code from:
http://code.activestate.com/recipes/580544-simple-drawing-tool-with-python-turtle-graphics/

"""
import turtle

# Create and set up screen and turtle.
t = turtle
# May need to tweak dimensions below for your screen.
t.setup(600, 600)
t.Screen()
t.title("Turtle Drawing Program - by Vasudev Ram")
t.showturtle()

# Set movement step and turning angle.
step = 160
angle = 45

def forward():
    '''Move forward step positions.'''
    print "forward", step
    t.forward(step)

def back():
    '''Move back step positions.'''
    print "back", step
    t.back(step)

def left():
    '''Turn left by angle degrees.'''
    print "left", angle
    t.left(angle)

def right():
    '''Turn right by angle degrees.'''
    print "right", angle
    t.right(angle)

def home():
    '''Go to turtle home.'''
    print "home"
    t.home()

def clear():
    '''Clear drawing.'''
    print "clear"
    t.clear()

def quit():
    print "quit"
    t.bye()

### add a pen up function



### add a pen down function


### add function change pen color to blue


### add function to change color back to black


### add a function to change the color to a custome turtle green color( #32D486)

t.onkey(forward, "Up")
t.onkey(left, "Left")
t.onkey(right, "Right")
t.onkey(back, "Down")
t.onkey(home, "h")
t.onkey(home, "H")
t.onkey(clear, "c")
t.onkey(clear, "C")
t.onkey(quit, "q")
t.onkey(quit, "Q")

t.listen()
t.mainloop()
