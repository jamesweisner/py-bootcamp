from googletrans.constants import LANGUAGES
import tkinter as tk
from deck import Deck

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        # Load up the deck of flashcards.
        # Prompt user for language on first run.
        self.deck = Deck()
        self.card = None

        # Initialize window.
        self.title('Loading...')
        self.config(padx=25, pady=25)

        # Set up widgets on a canvas.
        self.canvas = tk.Canvas(width=400, height=300)
        self.lang_text = self.canvas.create_text(200, 50, text='...', font=('Ariel', 25, 'italic'))
        self.word_text = self.canvas.create_text(200, 150, text='...', font=('Ariel', 50, 'bold'))
        self.canvas.config(bg='#bdc', highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=3, pady=(0, 25))
        self.canvas.bind('<Button-1>', self.peek)
        self.canvas.bind('<ButtonRelease-1>', self.peek)
        tk.Button(text=u'\u2716', font=('Ariel', 50), command=self.do_failure).grid(row=1, column=0)
        tk.Button(text=u'\U0001F50A', font=('Ariel', 50), command=self.speak).grid(row=1, column=1)
        tk.Button(text=u'\u2714', font=('Ariel', 50), command=self.do_success).grid(row=1, column=2)

        # Run the program.
        self.timer = None
        self.next()
        self.mainloop()

    def do_success(self):
        if self.card is not None:
            self.card.success()
            self.next()

    def do_failure(self):
        if self.card is not None:
            self.card.failure()
            self.next()

    def speak(self):
        if self.card is not None:
            self.card.speak()

    def peek(self, event):
        if self.timer is None:
            self.unflip() if event.type == tk.EventType.ButtonPress else self.flip()

    def next(self):
        if self.timer is not None:
            self.after_cancel(self.timer)
        self.card = self.deck.next()
        self.title(' - '.join([
            f'{LANGUAGES[self.deck.target].title()} Flashcards',
            f'Level {self.deck.level}',
            f'Cards {len(self.deck.queue)}',
        ]))
        self.unflip()
        self.timer = self.after(3000, func=self.flip)

    def unflip(self):
        self.canvas.itemconfig(self.lang_text, text=LANGUAGES[self.deck.target].title(), fill='#000')
        self.canvas.itemconfig(self.word_text, text=self.card.data['target'], fill='#000')
        self.canvas.config(bg='#bdc')

    def flip(self):
        self.canvas.itemconfig(self.lang_text, text=LANGUAGES[self.deck.native].title(), fill='#fff')
        self.canvas.itemconfig(self.word_text, text=self.card.data['native'], fill='#fff')
        self.canvas.config(bg='#597')
        self.timer = None

App() # Make it so.
