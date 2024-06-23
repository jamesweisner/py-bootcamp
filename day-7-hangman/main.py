from os import system
from string import ascii_uppercase
from random import choice
from hangman_art import logo, stages
from hangman_words import word_list

answer = list(choice(word_list).upper())
display = ['_'] * len(answer)
history = []
lives = 6
error = ''

while True:

    # Draw the current state of the game.
    system('clear')
    print(logo)
    print(stages[lives])
    print(f"   -= {' '.join(display)} =-\n")
    print(f"History: {' '.join(history)}")
    if lives == 0:
        print('You lose!')
        break
    if '_' not in display:
        print('You win!')
        break

    # Let the player guess a letter.
    print(f'{error}')
    guess = input('Guess a letter: ').upper().strip()
    if len(guess) != 1 or guess not in ascii_uppercase:
        error = 'Please type one letter.'
        continue
    if guess in history:
        error = 'You already guessed that letter.'
        continue
    error = ''
    history.append(guess)
    for i, letter in enumerate(answer):
        if letter == guess:
            display[i] = letter
    if guess not in answer:
        lives -= 1
