print("Welcome to Evil Treasure Island.")
print("Your mission is to acquire the treasure.")

island = {
    'start': {
        'about': 'From the dock you find yourself at a crossroads.',
        'prompt': 'Which way do you go?',
        'options': [
            ('Left', 'lake'),
            ('Right', 'hole'),
        ],
    },
    'hole': {
        'about': 'You fall down a sinkhole onto jagged rocks! There is no escape.',
    },
    'lake': {
        'about': 'You come to a lake. Something is moving in the water.',
        'prompt': 'What do you do?',
        'options': [
            ('Swim', 'shark'),
            ('Wait', 'arches'),
        ],
    },
    'shark': {
        'about': 'You are eaten by a shark!',
    },
    'arches': {
        'about':
            'While waiting you notice three stone arches.\n' \
            'Each has a different glyph carved into its capstone.',
        'prompt': 'Which do you approach?',
        'options': [
            ('Hand', 'fire'),
            ('Tree', 'win'),
            ('Bird', 'beasts'),
        ],
    },
    'fire': {
        'about':
            'You trigger a fire trap and are engulfed by flames!\n' \
            'You escape with only minor burns, but fail to find the treasure.',
    },
    'beasts': {
        'about':
            'You see a boar. And it sees you! He charges.\n' \
            'You manage to escape, but are forced to flee the island.',
    },
    'win': {
        'about':
            'You step through the stone arch and into a clearing.\n' \
            'A hollow tree stump sits at its ccenter...\n' \
            'Inside is a wooden box. This must be the treasure!',
        'prompt': 'Do you open the box?',
        'options': [
            ('Yes', 'flash'),
            ('No', 'wander'),
        ],
    },
    'flash': {
        'about': 'As you open the box it emits a flash of light!',
        'prompt': 'You find yourself back at the dock.',
        'options': [('Continue', 'start')],
    },
    'wander': {
        'about': 'You wander around the island and find yourself back at the dock.',
        'prompt': 'You find yourself back at the dock.',
        'options': [('Continue', 'start')],
    },
}

state = island['start']

while (True):
    print('\n' + '-' * 80 + '\n')
    print(state['about'])
    if 'options' not in state:
        print('\nGame over!')
        break
    while (True):
        options = ' or '.join([c for c, s in state['options']])
        choice = input(f"\n  > {state['prompt']} ({options}) ").strip().lower()
        found = False
        for c, s in state['options']:
            if len(choice) > 0 and c.lower().startswith(choice):
                state = island[s]
                found = True
                break
        if found:
            break
        else:
            print('\nBad input. Please try again.')
