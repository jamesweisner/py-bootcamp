from os import system
from random import choice
from setup import list_channels

def pick_channel(_a):
    """ Pick a new channel B having different number of subs from channel A. """
    while True:
        _b = choice(channels)
        if _a['subs'] != _b['subs']:
            return _b

def describe(c):
    """ Print out channel info: name, year started, and category. """
    message = f"{c['name']} started {c['year']}"
    if c['type'] != '':
        message += f" in {c['type']}"
    return message

def abbrev(n):
    """ Abbreviate number of subs with m for million. """
    return str(n / 1000000) + 'm'

# Load up top 1,000 YouTube channels.
channels = list_channels()

# Initialize game.
score = 0
a = None
b = choice(channels)

try:
    while True:

        # Start the next round.
        a = b
        b = pick_channel(a)

        # Print game state.
        system('clear')
        print(f'Your score: {score}\n')
        print('Which channel do you think is more popular?\n')
        print(f"  1: {describe(a)}")
        print(f"  2: {describe(b)}")

        # Player chooses one or the other channel.
        while True:
            channel = input('\n> ')
            print('')
            if channel in ['1', '2']:
                break
            print('Invalid choice.')

        # Check if the player guessed correctly.
        if (channel == '1') == (a['subs'] > b['subs']):
            score += 1
        else:
            print(f"  {a['name']} has {abbrev(a['subs'])} subs.")
            print(f"  {b['name']} has {abbrev(b['subs'])} subs.")
            input('\nGame over! Press enter to continue.')
            score = 0
            a = None
            b = choice(channels)
except KeyboardInterrupt:
    print('\n\nBye!')
