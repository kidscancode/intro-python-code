# KidsCanCode - Intro to Programming
import turtle
fred = turtle.Pen()
fred.speed(10)

colors = ["red", "orange", "yellow", "seagreen",
          "orchid", "royalblue", "dodgerblue"]

fred.up()
fred.goto(-320, -195)
fred.width(70)
# Draw the flag with a loop from the color list
for draw_color in colors:
    fred.color(draw_color)
    fred.down()
    fred.forward(640)
    fred.up()
    fred.backward(640)
    fred.left(90)
    fred.forward(66)
    fred.right(90)

fred.width(25)
fred.color("white")
fred.goto(0, -170)
fred.down()
fred.circle(170)  # draw the circle
fred.left(90)
fred.forward(340) # draw the vertical line
fred.left(180)
fred.forward(170) # go back to the center
fred.right(45)
fred.forward(170) # draw a leg
