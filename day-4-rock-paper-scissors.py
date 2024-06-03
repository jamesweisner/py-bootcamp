from random import randint

n = 1 + int(input('On a scale of 1 to 100, how brave are you? ')) * 2

while True:
    user = int(input(f'Choose a number between 1 and {n}: '))
    npc = randint(1, n)
    print(f'The computer chooses: {npc}')
    x = (n + user - npc) % n
    if x == 0:
        print('It\'s a tie.')
    elif x % 2 == 0:
        print('The computer wins!')
    else:
        print('You win!')
    print()
