import turtle
import random

fred = turtle.Pen()
fred.speed(10)
fred.width(2)

colors = ["red", "blue", "green", "turquoise"]

def triangle(length, width):
    fred.fillcolor(random.choice(colors))
    fred.begin_fill()
    for i in range(3):
        fred.color(random.choice(colors))
        fred.width(width)
        fred.forward(length)
        fred.left(120)
    fred.end_fill()

def star(length):
    for i in range(8):
        fred.color(random.choice(colors))
        fred.forward(length)
        fred.left(225)

for i in range(500):
    size = random.randrange(10, 100)
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    width = random.randrange(1, 15)
    fred.up()
    fred.goto(x, y)
    fred.down()
    triangle(size,width)
