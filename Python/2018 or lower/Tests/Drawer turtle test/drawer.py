# Made by Parker Cranfield
import turtle

turtle.setup(700, 700)
sc = turtle.Screen()


def f():
    turtle.forward(50)

def l():
    turtle.left(50)

def r():
    turtle.right(50)

def b():
    turtle.forward(-50)

sc.onkey(f, "Up")
sc.onkey(l, "Left")
sc.onkey(r, "Right")
sc.onkey(b, "Down")

sc.listen()

wait = input("")
