import turtle
import random
turtle = turtle.Turtle()
turtle.screen.tracer(0,0)
a = 1
turtle.speed(100)
colors = ['red', 'blue', 'black', 'green', 'purple', 'orange', 'pink', 'aquamarine', 'cyan', 'dark violet', 'indigo']
def hex(x):
    for n in range(6):
        turtle.forward(x)
        turtle.left(60)
for x in range(2):
    for x in range(3):
        for x in range(190):
            color_1 = random.choice(colors)
            turtle.color(color_1)
            hex(a)
            a += 1
        a = 1
        turtle.left(120)
    turtle.right(60)
