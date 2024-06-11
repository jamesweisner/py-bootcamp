from turtle import Turtle
from random import choice, randint, random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
BASE_SPEED = 5
BASE_NUM_CARS = 10

class Car(Turtle):

	def __init__(self, level):
		super().__init__('turtle')
		self.color(choice(COLORS))
		self.speed('fastest')
		self.shape('square')
		self.shapesize(stretch_len=2, stretch_wid=1)
		self.penup()
		x = randint(-570, 570)
		y = randint(-8, 8) * 30
		self.teleport(x, y)
		self.speed = (0.5 + random()) * level * BASE_SPEED

class CarManager:

	def __init__(self):
		self.cars = []
		self.level = 0
		self.next_level()

	def update(self):
		for car in self.cars:
			car.setx(car.xcor() - car.speed)
			if car.xcor() < -620:
				car.setx(620)

	def next_level(self):
		for car in self.cars:
			car.hideturtle()
			car.clear()
		self.cars.clear()
		self.level += 1
		while len(self.cars) < BASE_NUM_CARS + self.level:
			self.cars.append(Car(self.level))
