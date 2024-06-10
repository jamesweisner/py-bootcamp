from turtle import Turtle, Screen
from random import random


def get_color():
    r = random()
    g = (random() + r) / 2.0
    b = 1.0 - r
    return (r, g, b)


tim = Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, get_color())
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

Screen().exitonclick()
