# KidsCanCode - Intro to Programming
# Functions example using turtles - draw random shapes
import turtle
import random
fred = turtle.Pen()

colors = ["red", "green", "blue"]
fred.speed(20)

# Define how to draw a square
def square(length):
    for i in range(4):
        fred.forward(length)
        fred.left(90)

# Define how to draw a triangle
def triangle(length):
    for i in range(3):
        fred.forward(length)
        fred.left(120)

for i in range(100):
    x = random.randrange(-200, 200)   # Pick a random number for x
    y = random.randrange(-200, 200)   # Pick a random number for y
    size = random.randrange(10, 100)  # Pick a random size for the shape
    c = random.choice(colors)         # Pick a random color
    width = random.randrange(1, 10)   # Pick a random line width
    fred.up()                         # Pick up the pen before we move
    fred.goto(x,y)                    # Go to the random coordinate
    fred.down()                       # Don't forget to put the pen down
    fred.color(c)                     # Set the color
    fred.width(width)                 # Set the width
    triangle(size)                    # Draw the shape!

    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    size = random.randrange(10, 100)
    c = random.choice(colors)
    width = random.randrange(1, 10)
    fred.up()
    fred.goto(x,y)
    fred.down()
    fred.color(c)
    fred.width(width)
    square(size)
