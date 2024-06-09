from string import ascii_lowercase

ALPHABET = list(ascii_lowercase)


def caesar(message, shift_amount):
    output = ''
    for c in message:
        try:
            position = (ALPHABET.index(c) + shift_amount) % 26
            output += ALPHABET[position]
        except:
            # Non-alphabetical characters just get copied.
            output += c
    return output


def run_program():

    # Prompt user to choose an encription mode.
    while True:
        mode = input('[E]ncode or [D]ecode? ').strip().lower()
        if 'encode'.startswith(mode) or 'decode'.startswith(mode):
            break
        else:
            print('Invalid encryption mode.')
            print('Please type "E" to encode or "D" to decode.')

    # Prompt user to choose a cipher key.
    while True:
        key = int(input('Cipher key: '))
        if key > 0:
            break
        else:
            print('Invalid cipher key.')
            print('Please enter a positive integer.')

    # Prompt user for input message.
    while True:
        message = input('Input message: ').strip().lower()
        if len(message) > 0:
            break
        else:
            print('Please enter a message.')

    # Calculate shift amount.
    shift_amount = key % 26
    if 'decode'.startswith(mode):
        shift_amount = 26 - shift_amount

    # Encrypt or decrypt the message.
    print('Output message: ' + caesar(message, shift_amount))


try:
    while True:
        run_program()
        print('\nPress ctl-C at any time to end this program.\n')
except KeyboardInterrupt:
    print('')
