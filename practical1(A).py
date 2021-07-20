import turtle

s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("lightblue")
t.pensize(width=7)
t.pencolor("red")
t.shape("circle")
t.fillcolor("red")
t.speed(1)

def draw(s):
    for i in range(4):
        t.fd(s)
        t.pu()
        t.goto(0,0)
        t.pd()
        t.lt(90)

draw(300)