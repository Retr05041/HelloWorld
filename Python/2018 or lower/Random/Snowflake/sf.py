# Make snowflakes with turtles
# By Carrie Anne Philbin
# Made by Parker Cranfield by referencing them ^

import turtle
import random

# Setup the window with a background color
turtle.setup(700, 700)
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
elsa = turtle.Turtle()
elsa.speed(0)

# Create colors
sfcolor = "grey"

# Define a function to create different sized snowflakes
def snowflake(size):
  # move the pen into starting position
  elsa.penup()
  elsa.forward(10 * size)
  elsa.left(45)
  elsa.pendown()
  elsa.color(sfcolor)
  # draw branch 8 times to make a snowflake
  for i in range(8):
    branch(size)
    elsa.left(45)

# This function creates one branch of the snowflake
def branch(size):
  for i in range(3):
    for i in range(3):
      elsa.forward(10.0 * size / 3)
      elsa.back(10.0 * size / 3)
      elsa.right(45)
    elsa.left(90)
    elsa.back(10.0 * size / 3)
    elsa.left(45)
  elsa.right(90)
  elsa.forward(10.0 * size)

# Loop to create 20 snowflakes of different sizes and at
# different starting locations
for i in range(50):
  x = random.randint(-200, 200)
  y = random.randint(-200, 200)
  sfsize = random.randint(1, 4)
  elsa.penup()
  elsa.goto(x, y)
  elsa.pendown()
  snowflake(sfsize)
