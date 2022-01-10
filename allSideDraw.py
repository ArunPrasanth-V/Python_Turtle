from random import randint, randrange
from turtle import Turtle, Screen, colormode
tom=Turtle()
colormode(255)
screen=Screen()
def move(side):
    angle=360/side

    for ii in range(side):
        tom.color(randrange(0, 257, 10),randrange(0, 257, 10),randrange(0, 257, 10))
        tom.forward(100)
        tom.right(angle)

for i in range(2,10):
    move(i)

screen.exitonclick()
