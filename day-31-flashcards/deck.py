from requests import get
from os.path import join
from json import dump, load
from string import ascii_lowercase
from googletrans.constants import LANGUAGES
from card import Card, BadWordError

class Deck:

    def __init__(self):

        # Load language profile.
        profile = join('data', 'profile.json')
        try:
            with open(profile) as file:
                self.target, self.native = load(file)
        except FileNotFoundError:
            self.target = input('Target language? (The one you want to learn.) ').lower().strip()
            self.native = input('Native language? (The one you already know.) ').lower().strip()
            assert self.target in LANGUAGES
            assert self.native in LANGUAGES
            with open(profile, 'w') as file:
                dump([self.target, self.native], file)

        # Load cards file.
        try:
            with open(self.data_file('cards')) as file:
                self.cards = {c['target']: Card(c, self, 0) for c in load(file)}
        except FileNotFoundError:
            self.cards = {}

            # Download 50k most common words in target language.
            data = get('/'.join([
                'https://raw.githubusercontent.com/hermitdave/FrequencyWords',
                f'master/content/2018/{self.target}/{self.target}_50k.txt',
            ])).text

            # Clean up the list, removing nonsense words where possible.
            for line in data.splitlines():
                word, uses = line.split(' ')
                if not all([c in ascii_lowercase for c in word]):
                    continue # Looks sus.
                self.cards[word] = Card({ 'target': word, 'uses': int(uses) }, self, None)

        # Begin or resume session.
        try:
            with open(self.data_file('session')) as file:
                session = load(file)
                self.level = session['level']
                self.queue = session['queue']
                self.boxes = session['boxes']
                for i, words in enumerate(self.boxes):
                    for word in words:
                        self.cards[word].box_id = i
        except FileNotFoundError:
            self.level = 0
            self.queue = []
            self.boxes = [[]]
            i = 0
            for c in sorted(self.cards.values(), key=lambda c: c.data['uses'], reverse=True):
                self.boxes[i].append(c.data['target'])
                c.box_id = i
                if len(self.boxes[i]) == 10:
                    self.boxes.append([]) # Create another box.
                    i += 1 # Start populating this new box.

    def save(self):
        with open(self.data_file('cards'), 'w') as file:
            dump([c.data for c in self.cards.values()], file)
        with open(self.data_file('session'), 'w') as file:
            dump({
                'level': self.level,
                'queue': self.queue,
                'boxes': self.boxes,
            }, file)

    def next(self):
        while True:
            if len(self.queue) < 1:
                if self.level < 1 or len(self.boxes[0]) < 10:
                    self.level += 1 # Level up unless missed 10 or more.
                else:
                    print('You missed 10 or more. Replaying level.')
                for i in range(self.level):
                    for w in self.boxes[i]:
                        self.queue.append(w)
                print(f'Starting level {self.level} with {len(self.queue)} cards.')
            card = self.cards[self.queue[0]]
            try:
                card.translate()
                break
            except BadWordError:
                print(f"Removing card: {card.data['target']}")
                self.boxes[card.box_id].remove(card.data['target'])
                del self.cards[card.data['target']]
                self.queue.pop(0)
        self.save()
        return card

    def data_file(self, name):
        return join('data', f'{self.target}-{self.native}-{name}.json')
