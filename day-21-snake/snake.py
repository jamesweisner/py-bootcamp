from turtle import Turtle

class Snake:

	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		for position in [(0, -20 * i) for i in range(3)]:
			self.add_segment(position)

	def add_segment(self, position):
		new_segment = Turtle('square')
		new_segment.color('white')
		new_segment.penup()
		new_segment.goto(position)
		self.segments.append(new_segment)

	def extend(self):
		self.add_segment(self.segments[-1].position())

	def move(self):
		for i in range(len(self.segments) - 1, 0, -1):
			self.segments[i].goto(self.segments[i - 1].position())
		self.head.forward(20)

	def turn(self, heading):
		if abs(self.head.heading() - heading) != 180:
			self.head.setheading(heading)
