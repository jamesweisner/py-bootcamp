from random import randint

answer = randint(1, 100)

try:
    while True:
        try:
            mode = input('\n[E]asy or [H]ard mode? ').strip().lower()
            assert len(mode) > 0
            if 'easy'.startswith(mode):
                guesses = 10
                break
            elif 'hard'.startswith(mode):
                guesses = 5
                break
            else:
                assert False
        except Exception:
            pass

    print(f'\nChoose a number between 1 and 100. You have {guesses} guesses.')

    while True:
        try:
            guess = int(input('\n> '))
            assert guess >= 1 and guess <= 100
        except ValueError:
            print("\nThat's not even, like, a number?")
        except AssertionError:
            print(f'\nDo you really think {guess} is between 1 and 100?')
        else:
            if guess == answer:
                break
            hint = 'high' if guess > answer else 'low'
            guesses -= 1
            if guesses < 1:
                break
            print(f'\nToo {hint}. You have {guesses} guesses left.')

    if guesses > 0:
        print('\nYou win!\n')
    else:
        print('\nSorry, out of guesses.\n')

except KeyboardInterrupt:
    print('\n\nBye!\n')
