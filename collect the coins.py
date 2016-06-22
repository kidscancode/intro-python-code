from tkinter import *
import time
import random

WIDTH = 800
HEIGHT = 600

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
tk.title("Moving around")
canvas.pack()

player = canvas.create_rectangle(0, 0, 50, 50, fill="red")

def move(event):
    canvas.coords(player, event.x, event.y, event.x+50, event.y+50)

canvas.bind("<Motion>", move)

def make_coin():
    x = random.randrange(WIDTH - 30)
    y = random.randrange(HEIGHT - 30)
    coin = canvas.create_oval(x, y, x+30, y+30, fill="gold")
    return coin

coins = []
for i in range(10):
    coins.append(make_coin())

level = 1
score = 0
timer = 30
time_limit = 30
time_started = time.time()
score_label = canvas.create_text(5, 5, anchor=NW, text="Score: 0", fill="white",
                                 font=('Arial', 24))
time_label = canvas.create_text(5, 45, anchor=NW, text="Timer: 30", fill="white",
                                 font=('Arial', 24))

while timer > 0:
    timer = time_limit - int(time.time() - time_started)
    canvas.itemconfig(score_label, text="Score: "+str(score))
    canvas.itemconfig(time_label, text="Timer: "+str(timer))
    pos = canvas.coords(player)
    hits = canvas.find_overlapping(*pos)
    for coin in coins:
        if coin in hits:
            score += 10
            canvas.delete(coin)
            coins.remove(coin)
    if len(coins) == 0:
        level += 1
        for i in range(level * 10):
            coins.append(make_coin())
    tk.update()
    time.sleep(0.01)
