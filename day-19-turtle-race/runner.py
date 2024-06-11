from turtle import Turtle
from random import randint


class Runner:

    def __init__(self, color, pos):
        self.t = Turtle(shape='turtle')
        self.t.penup()
        self.t.color(color)
        self.t.goto(x=-230, y=pos)

    def advance(self):
        self.t.forward(randint(0, 10))

    def name(self):
        return self.t.pencolor()

    def has_won(self):
        return self.t.xcor() > 230


def Runners():
    return [
        Runner('red', -70),
        Runner('orange', -40),
        Runner('yellow', -10),
        Runner('green', 20),
        Runner('blue', 50),
        Runner('purple', 80),
    ]
