import random
from  turtle import  Turtle

dot = Turtle()

POSITION = (0, -340)


class Ball():
    def __init__(self):
        self.create()
        self.create_dash()
    def create(self):
        dot.hideturtle()
        dot.penup()
        dot.pencolor("white")
        dot.goto(0, -290)
    def create_dash(self):
        for dash in range(29):
            dot.pensize(5)
            dot.setheading(90)
            dot.forward(10)
            dot.penup()
            dot.forward(10)
            dot.pendown()

