from pandas import read_csv

alphabet = read_csv('alphabet.csv', index_col='letter').to_dict()['code']

try:
    while True:
        word = input('Enter a word: ').upper()
        letters = [alphabet[c] for c in word if c in alphabet]
        print(' > ' + ' • '.join(letters) + '\n')
except KeyboardInterrupt:
    pass # Just exit.
