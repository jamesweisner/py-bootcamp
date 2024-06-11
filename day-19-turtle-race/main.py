from runner import Runners
from turtle import Screen

screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput('Make your bet', 'Which runner will win the race?')
print(f'You bet on the {guess} turtle.')
runners = Runners()

race_over = False
while not race_over:
    for runner in runners:
        runner.advance()
        if runner.has_won():
            print(f"The {runner.name()} turtle is the winner!")
            win = runner.name().startswith(guess.strip().lower())
            print(f"You {'win' if win else 'lose'}!")
            race_over = True
            break

screen.exitonclick()
