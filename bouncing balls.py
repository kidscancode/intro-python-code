from tkinter import *
import time
import random

WIDTH = 800
HEIGHT = 500

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
tk.title("Drawing")
canvas.pack()

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta',
          'dodgerblue', 'turquoise', 'grey', 'gold', 'pink']

class Ball:
    def __init__(self):
        self.size = random.randrange(200, 400)
        color = random.choice(colors)
        self.shape = canvas.create_rectangle(0, 0, self.size, self.size, fill=color)
        self.speedx = random.randrange(1, 10)
        self.speedy = random.randrange(1, 10)

    def update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

ball_list = []
for i in range(100):
    ball_list.append(Ball())
while True:
    for ball in ball_list:
        ball.update()
    tk.update()
    time.sleep(0.01)
