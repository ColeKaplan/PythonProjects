import turtle
t=turtle.Turtle()
#t.screen.tracer(0,0)
screen = turtle.Screen()
screen.bgcolor('blue')
t.color('white')
t.speed(10000000000)
def snowflake(x):
    for l in range(4):
        t.forward(x)
        t.left(90)
        t.forward(x/2)
        for i in range(4):
            t.right(45)
            t.forward(x/3)
            t.right(90)
            t.forward(x/3)
for i in range(9):
    snowflake(80)
    t.left(45)
