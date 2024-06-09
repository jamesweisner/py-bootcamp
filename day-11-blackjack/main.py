from game import Game


def choose(prompt, options):
    while True:
        choice = input(f'{prompt} ').strip().lower()
        if len(choice) < 1:
            continue  # Try again.
        for o in options:
            if o.startswith(choice):
                return o


while True:
    game = Game()
    game.draw()
    while not game.over:
        move = choose('Would you like to [H]it or [S]tand?', ['hit', 'stand'])
        getattr(game, move)()
        game.draw()
    response = choose('[P]lay another game or [Q]uit?', ['play', 'quit'])
    if response == 'quit':
        print('\nBye!\n')
        break
