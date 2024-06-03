from random import choice, shuffle

letters = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
letters += [c.lower() for c in letters]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Evil Password Generator!")

n_letters = int(input("How many letters in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

password = [choice(letters) for i in range(n_letters)]
password += [choice(symbols) for i in range(n_symbols)]
password += [choice(numbers) for i in range(n_numbers)]

shuffle(password)

print('\n  Password: ' + ''.join(password))
