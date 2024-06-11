from os.path import join

with open(join('Input', 'Letters', 'starting_letter.txt')) as file:
	data = file.read()

with open(join('Input', 'Names', 'invited_names.txt')) as file:
	names = [line.strip() for line in file]

for name in names:
	filename = f"letter_for_{name.replace(' ', '_')}.txt"
	with open(join('Output', 'ReadyToSend', filename), 'w') as file:
		file.write(data.replace('[name]', name))
