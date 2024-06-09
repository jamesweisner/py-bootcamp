from random import choices

from replit import clear

from items import ITEMS

item = choices(ITEMS, weights=[i['weight'] for i in ITEMS])[0]

bidders = []

while True:

    print('Welcome to the secret auction!')
    print(f"Okay! Here's our next item: {item['name']}")

    # Name.
    while True:
        try:
            name = input('What is your name? ').strip().title()
            assert len(name) > 0
            assert 'Kefka' not in name
            break
        except Exception:
            print("Sorry, I didn't catch your name...?")

    # Bid.
    while True:
        try:
            bid = int(input('What is your bid? '))
            assert bid > 0
            break
        except Exception:
            print('Please enter a positive integer.')

    bidders.append({'name': name, 'bid': bid})
    print(f'Thank you, {name}! Your bid for {bid} has been recorded.')

    # Loop.
    while True:
        try:
            loop = input('Are there more bidders? [Y/N] ').strip().lower()
            assert 'yes'.startswith(loop) or 'no'.startswith(loop)
            break
        except Exception:
            print('Please type "Y" or "N".')

    clear()  # Always clear the screen to protect bidder privacy.

    if 'no'.startswith(loop):
        # Done taking bids!
        break

winner = max(bidders, key=lambda b: b['bid'])

if item['bid'] is None or item['bid'] > winner['bid']:
    winner = {'name': 'Kefka', 'bid': winner['bid'] + 1}

print(f"The winner is {winner['name']} with a bid of {winner['bid']}!")
