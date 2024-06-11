from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1200, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

def game_loop():
	while True:
		screen.update()
		sleep(0.1)
		car_manager.update()
		player.update()
		for car in car_manager.cars:
			if player.distance(car) < 20: # TODO fix
				return
		if player.has_won():
			player.reset()
			car_manager.next_level()
			scoreboard.increase_score()

game_loop()
scoreboard.game_over()
screen.exitonclick()
