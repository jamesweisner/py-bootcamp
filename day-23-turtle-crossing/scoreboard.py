from turtle import Turtle

FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.speed('fastest')
		self.color('black')
		self.hideturtle()
		self.teleport(0, 270)
		self.score = 0
		self.update_scoreboard()

	def update_scoreboard(self):
		self.write(f'Score: {self.score}', align='center', font=FONT)

	def game_over(self):
		self.teleport(0, 0)
		self.write('GAME OVER', align='center', font=FONT)

	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_scoreboard()
