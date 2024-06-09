from json import loads
from os import system
from random import choice


def pick_channel(a):
    """ Pick a new channel B having different number of subs from channel A. """
    while True:
        b = choice(channels)
        if a['subs'] != b['subs']:
            return b


def describe(c):
    """ Print out channel info: name, year started, and category. """
    message = f"{c['name']} started {c['year']}"
    if c['type'] != '':
        message += f" in {c['type']}"
    return message


def abbrev(n):
    """ Abbreviate number of subs with m for million. """
    return str(n / 1000000) + 'm'


# Load up top 1,000 channels generated by setup.py.
with open('channels.json', encoding='utf-8') as file:
    channels = loads(file.read())

# Initialize game.
score = 0
a = None
b = choice(channels)

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
