from random import choice
from pandas import read_csv

class Game:

	def __init__(self, file):
		self.file = file
		self.score = 0
		self.bonus_amount = 0
		self.bonus_states = []
		self.states = read_csv(self.file, index_col='name')
		self.remaining = self.states.index.to_list()

	def save(self, file):
		self.file = file
		self.states.to_csv(self.file)

	def guess(self, state):
		if not state in self.remaining:
			return None
		self.remaining.remove(state)
		self.score += 1
		if state in self.bonus_states:
			self.score += self.bonus_amount
		row = self.states.loc[state, ['x', 'y']]
		return map(int, row)

	def title(self):
		return f'Named {50 - len(self.remaining)}/50 States'

	def prompt(self):
		guessed = 50 - len(self.remaining)
		if guessed < 1:
			return 'Name a State, any State!'
		if guessed < 10:
			return "What's another state's name?"
		if guessed < 20:
			letter = choice(self.remaining)[0]
			self.bonus_amount = 1
			self.bonus_states = [s for s in self.remaining if s.startswith(letter)]
			return f'Bonus +1: Starts with "{letter}".'
		if guessed < 30:
			self.bonus_amount = 2
			self.bonus_states = [choice(self.remaining)]
			capital = self.states.loc[self.bonus_states[0], 'capital']
			return f'Bonus +2: Capital is {capital}.'
		if guessed < 40:
			self.bonus_amount = 3
			self.bonus_states = [choice(self.remaining)]
			bird = self.states.loc[self.bonus_states[0], 'bird']
			return f'Bonus +3: State bird is {bird}!'
		else:
			self.bonus_amount = 4
			self.bonus_states = [choice(self.remaining)]
			flower = self.states.loc[self.bonus_states[0], 'flower']
			return f'Bonus +4: State flower is {flower}!'
