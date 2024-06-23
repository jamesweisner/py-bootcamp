from os import environ

# Don't output junk to my console, please.
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from googletrans import Translator
from os.path import join, isfile
from pygame import mixer
from os import makedirs
from gtts import gTTS

mixer.init()
translator = Translator()

class BadWordError(Exception):
    pass

# Cards are words in the target language.
# They know how to:
#   - Get their native translation.
#   - Speak the word in target language.
#   - Work in a spaced repetition learning system.
class Card:

    def __init__(self, data, deck, box_id):
        self.data = data
        self.deck = deck
        self.box_id = box_id

    def translate(self):
        if 'native' not in self.data:
            r = translator.translate(self.data['target'], src=self.deck.target, dest=self.deck.native)
            if r.text.lower() == self.data['target']:
                raise BadWordError()
            self.data['native'] = r.text.lower()

    def speak(self):
        cache = join('sounds', f'{self.deck.target}-{self.data['target']}.mp3')
        if not isfile(cache):
            makedirs('sounds', exist_ok=True)
            gTTS(text=self.data['target'], lang=self.deck.target, slow=False).save(cache)
        mixer.music.load(cache)
        mixer.music.play(loops=0)

    def move_to(self, new_id):
        self.deck.boxes[self.box_id].remove(self.data['target'])
        self.box_id = new_id
        self.deck.boxes[self.box_id].append(self.data['target'])
        self.deck.queue.pop(0) # Should always be this card.

    def success(self):
        self.move_to(self.box_id + 1)

    def failure(self):
        self.move_to(0)
