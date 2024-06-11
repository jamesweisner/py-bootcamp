from turtle import Turtle
from random import randint

class Food(Turtle):

	def __init__(self):
		super().__init__()
		self.shape('circle')
		self.penup()
		self.shapesize(stretch_len=0.75, stretch_wid=0.75)
		self.color('blue')
		self.speed('fastest')
		self.refresh()

	def refresh(self):
		x = randint(-13, 13) * 20
		y = randint(-13, 13) * 20
		self.goto(x, y)
