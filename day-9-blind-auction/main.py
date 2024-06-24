from random import choices
from os import system, name as os_name
from json import load
from pygame import mixer
from time import sleep

def snazzy_input(prompt, retry, filter=lambda r: r.strip(), checker=lambda r: True):
    while True:
        try:
            response = filter(input(prompt + ' '))
            assert checker(response)
            return response
        except Exception:
            print(retry)

# Gotta have that auction house music!
mixer.init()
mixer.music.set_volume(0.5)
mixer.music.load('music.mid')
mixer.music.play()

# Separate code & data with auction items stored in JSON format.
with open('items.json') as file:
    items = load(file)

item = choices(items, weights=[i['weight'] for i in items])[0]

highest = 0
winner = None

while True:

    print('Welcome to the blind auction!')
    print(f"Okay! Here's our next item: {item['name']}")

    name = snazzy_input(
        prompt='What is your name?',
        retry="Sorry, I didn't catch your name...?",
        filter=lambda r: r.strip().title(),
        checker=lambda r: len(r) > 0 and 'Kefka' not in r
    )

    bid = snazzy_input(
        prompt='What is your bid?',
        retry='Please enter a positive integer.',
        filter=lambda r: int(r),
        checker=lambda r: r > 0
    )

    print(f'Thank you, {name}! Your bid for {bid:,} has been recorded.')

    # Largest bid wins. First to bid wins ties.
    if bid > highest:
        highest = bid
        winner = name

    loop = snazzy_input(
        prompt='Are there more bidders?',
        retry='Please enter "Yes" or "No".',
        filter=lambda r: r.strip().lower(),
        checker=lambda r: 'yes'.startswith(r) or 'no'.startswith(r)
    )

    # Clear the screen to protect bidder privacy.
    system('cls' if os_name == 'nt' else 'clear')

    if 'no'.startswith(loop):
        break # Done taking bids!

# Kefka cheats.
if item['bid'] is None or item['bid'] > highest:
    highest += 1
    winner = 'Kefka'

print(f"The winner is {winner} with a bid of {highest:,}!")

mixer.music.fadeout(1000)
sleep(1)
mixer.music.stop()
