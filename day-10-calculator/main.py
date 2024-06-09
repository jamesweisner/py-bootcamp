from calc import OPERATORS, calc

print('Welcome to the Calculon 2.0 app!')
print('It does "some" math pretty well.')
print('Press ctl-C at any time to exit.')

ALLOWED = [str(i) for i in range(10)] + [o[0] for o in OPERATORS]

history = []

try:
    print('')
    while True:
        expression = input('> ').replace(' ', '')
        if expression in history:
            print('\nDoes anyone here not have amnesia?\n')
            continue
        else:
            history.append(expression)
        if not set(expression).issubset(ALLOWED):
            print('\nInvalid expression!')
            print('I only recognize integer numbers...')
            print('And the "MDAS" operators!\n')
        else:
            try:
                print('= ' + str(calc(expression)) + '\n')
            except Exception as e:
                print('Error: ' + str(e))
                print('That was so terrible...')
                print('I think you gave me cancer!\n')
except KeyboardInterrupt:
    print('\n\nThe name Calculon used to mean something...')
    print("Now it's a stain that will never wash clean.")
