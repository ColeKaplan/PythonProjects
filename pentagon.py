import turtle
import random
turtle = turtle.Turtle()
a = 1
turtle.screen.tracer(0,0)
turtle.speed(100)
colors = ['red', 'blue', 'black', 'green', 'purple', 'orange', 'pink', 'aquamarine', 'cyan', 'dark violet', 'indigo']
def pent(x):
    for n in range(5):
        turtle.forward(x)
        turtle.left(72)
for x in range(100):
    for x in range(100):
        pent(a)
        color_1 = random.choice(colors)
        turtle.color(color_1)
        a += 1
    a = 1
    turtle.left(108)
