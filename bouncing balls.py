# Animated bouncing balls
# KidsCanCode - Intro to Programming
from tkinter import *
import random
import time

# Define ball properties and functions
class Ball:
    def __init__(self, canvas, color, size):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,size,size, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.yspeed = -1
        self.xspeed = random.randrange(-3, 3)

    def draw(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.yspeed = random.randrange(1,10)
        if pos[3] >= 400:
            self.yspeed = random.randrange(-10,-1)
        if pos[0] <= 0:
            self.xspeed = random.randrange(1,10)
        if pos[2] >= 500:
            self.xspeed = random.randrange(-10,-1)

# Create window and canvas to draw on
tk = Tk()
tk.title("Game")
canvas = Canvas(tk, width=500, height=400, bd=0)
canvas.pack()
tk.update()

# Create a list of 20 balls, each with a random size and color
ball_list = []
color_list = ['blue', 'red', 'green', 'papaya whip', 'brown', 'lavender']
for i in range(20):
    color = random.choice(color_list)
    size = random.randrange(10, 100)
    ball_list.append(Ball(canvas, color, size))

# Animation loop
while True:
    # animate each ball in the list of balls
    for ball in ball_list:
        ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
