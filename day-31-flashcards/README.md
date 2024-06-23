I made several noteworthy improvements to this capstone project:

1. The user can choose which language they want to study when they first launch the program. They're also asked their native language, in case it's not English. Strings are translated using Google Translate on the fly. Cards containing loaner words (i.e. same word on both sides) are automatically removed from the deck.

2. There's a 🔉 button in between the ✘ and ✔ buttons to speak the word aloud using Google TTS. These sound files downloaded from the Internet are cached locally.

3. I implemented a variety of spaced repetition learning system. The user starts at level 1 with 10 words, then goes on to level 2 with 20 words, etc.

4. I use unicode for the buttons and tkinter to draw the card, so there's no need for any image files.

5. Use JSON to save state instead of CSV which eliminates the need for pandas library. Fewer dependancies are better.
