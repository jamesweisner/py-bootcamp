from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
for k, h in {'Up': 90, 'Down': 270, 'Left': 180, 'Right': 0}.items():
	screen.onkey(lambda h=h: snake.turn(h), k)

def game_loop():

	while True:

		screen.update()
		time.sleep(0.1)
		snake.move()

		# Detect collision with food.
		if snake.head.distance(food) < 15:
			food.refresh()
			snake.extend()
			scoreboard.increase_score()

		# Detect collision with wall.
		for cor in snake.head.position():
			if abs(cor) > 280:
				return

		# Detect collision with tail.
		for segment in snake.segments[1:]:
			if snake.head.distance(segment) < 10:
				return

game_loop()
scoreboard.game_over()
screen.exitonclick()
