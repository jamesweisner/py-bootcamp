from requests import post, get
from random import choices
from string import ascii_letters, digits
from json import loads

class Pixela:

	endpoint = "https://pixe.la/v1/users"

	def __init__(self, username, token):
		self.username = username
		self.token = token

	def register(self):
		self.token = ''.join(choices(ascii_letters + digits, k=16))
		return self.post("/", {
		    "token": self.token,
		    "username": self.username,
		    "agreeTermsOfService": "yes",
		    "notMinor": "yes",
		})

	def create(self):
		try:
			self.post(f"/{self.username}/graphs", {
				"id": "steps",
				"name": "Step Counter",
				"unit": "step",
				"type": "int",
				"color": "sora",
			})
		except Exception as e:
			if "This graphID already exist" not in str(e):
				raise e

	def set_pixel(self, date, quantity):
		self.post(f"/{self.username}/graphs/steps", {
		    "date": date,
		    "quantity": str(quantity),
		})
		with open('latest.txt', 'w') as file:
			file.write(date)

	def get_latest(self):
		# There's an API to get latest pixel, but it's paywalled.
		# It will only return the latest pixel in the past year.
		# https://docs.pixe.la/entry/get-latest-pixel
		try:
			with open('latest.txt') as file:
				return file.read()
		except FileNotFoundError:
			return None

	def get_url(self):
		return f"{self.endpoint}/{self.username}/graphs/steps.html"

	def headers(self):
		return {"X-USER-TOKEN": self.token} if self.token else None

	def handle(self, response):
		if response.status_code == 200:
			return loads(response.text) # Return entire payload on success.
		if not response.text:
			raise Exception("Empty response.")
		raise Exception(loads(response.text)["message"])

	def get(self, uri):
		while True:
			try:
				return self.handle(get(url=f"{self.endpoint}{uri}", headers=self.headers()))
			except Exception as e:
				if 'Please retry this request' not in str(e):
					raise e

	def post(self, uri, data):
		while True:
			try:
				return self.handle(post(url=f"{self.endpoint}{uri}", json=data, headers=self.headers()))
			except Exception as e:
				if 'Please retry this request' not in str(e):
					raise e
