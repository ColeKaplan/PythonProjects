import turtle
import random
turtle = turtle.Turtle()
turtle.speed(100)
a = 1
turtle.screen.tracer(0,0)
colors = ['red', 'blue', 'black', 'green', 'purple', 'orange', 'pink', 'aquamarine', 'cyan', 'dark violet', 'indigo']
def hept(l):
    for x in range(7):
        turtle.forward(a)
        turtle.left(51.4285714286)
for x in range(6):
    for x in range(200):
        color_1 = random.choice(colors)
        turtle.color(color_1)
        hept(a)
        a += 1
    a = 1
    turtle.left(128.571428571)
