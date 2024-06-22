from hashlib import sha1
from os.path import isfile
from json import loads, dumps
from random import choice, shuffle
from string import ascii_letters, digits, punctuation

CHARACTERS = ascii_letters + digits + punctuation
FILENAME = 'passwords.json'

class Database:

	def __init__(self, password):
		self.password = password
		if not isfile(FILENAME):
			self.records = []
			self.save()
			return
		with open(FILENAME) as file:
			self.records = loads(file.read())
		for r in self.records:
			decrypted = ''
			salt = r['Website']
			for c in r['Password']:
				rotate = self.hash(salt)
				salt = CHARACTERS[(CHARACTERS.find(c) + rotate) % len(CHARACTERS)]
				decrypted += salt
			r['Password'] = decrypted
		print(f"Loaded {len(self.records)} record{'s' if len(self.records) > 1 else ''}!")

	def save(self):
		data = self.records.copy()
		for r in data:
			encrypted = ''
			salt = r['Website']
			for c in r['Password']:
				rotate = len(CHARACTERS) - self.hash(salt)
				encrypted += CHARACTERS[(CHARACTERS.find(c) + rotate) % len(CHARACTERS)]
				salt = c
			r['Password'] = encrypted
		with open(FILENAME, 'w') as file:
			file.write(dumps(data))
		print('Saved!')

	def hash(self, salt):
		encoded = (self.password + salt).encode('utf-8')
		return int(sha1(encoded).hexdigest(), 16) % len(CHARACTERS)

	def generate(self):
		return ''.join(choice(CHARACTERS) for _ in range(16))

	def save_record(self, data):
		r = self.find_record(data['Website'])
		if r is None:
			self.records.append(data)
		else:
			for label in ['Username', 'Password']:
				r[label] = data[label]
		self.save()

	def find_record(self, website):
		for r in self.records:
			if r['Website'] == website:
				return r
		return None

	def default_username(self):
		try:
			return self.records[-1]['Username']
		except IndexError:
			return '' # Empty database.

	def bg_color(self):
		return '#' + ''.join(sha1(self.password.encode('utf-8')).hexdigest()[:6])
