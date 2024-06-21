from turtle import Turtle, Screen, shape
from game import Game

screen = Screen()
screen.setup(width=725, height=491)
screen.addshape('map.gif')
shape('map.gif')

game = Game('states-v2.csv')

while True:
	screen.title(f'US States Game (score: {game.score})')
	state = screen.textinput(title=game.title(), prompt=game.prompt())
	if state is None:
		break # User wants to quit.
	try:
		x, y = game.guess(state)
		t = Turtle()
		t.speed('fastest')
		t.hideturtle()
		t.penup()
		t.goto(x, y)
		t.write(state)
	except TypeError:
		pass
	if len(game.remaining) == 0:
		break # User won the game!

screen.exitonclick()
