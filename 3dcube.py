from turtle import *
from time import sleep as sl

t=Turtle()
t.color('red')
setup(500,500)

t.forward(100)
t.right(90)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)

t.penup()
t.goto(50,50)

t.pendown()
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)


t.penup()
t.left(90)
t.forward(100)

t.pendown()
t.goto(0, 100)

t.penup()
t.goto(50,50)

t.pendown()
t.goto(100, 100)

t.penup()
t.goto(100, 0)

t.pendown()
t.goto(50, -50)

t.penup()
t.goto(-50, -50)

t.pendown()
t.goto(0, 0)

t.penup()
t.goto(200, 200)

sl(5)
