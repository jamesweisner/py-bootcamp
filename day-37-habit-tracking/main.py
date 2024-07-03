from pixela import Pixela
from health import Health
from json import load, dump
from subprocess import call

# Register and create a Pixela graph. This only has to happen once.
# To avoid losing access to your account, please back up your credentials!
try:
	with open("credentials.json") as file:
		username, token = load(file)
		pixela = Pixela(username, token)
except FileNotFoundError:
	while True:
		username = input("Please enter a username: ")
		pixela = Pixela(username, None)
		try:
			pixela.register()
			break
		except Exception as e:
			print(f"Registration failed: {e}\n")
	with open("credentials.json", "w") as file:
		dump([username, pixela.token], file)

pixela.create()

# Extract records from the iOS Health app.
try:
	health = Health("export.zip")
	health.extract("steps.json")
except FileNotFoundError:
	exit("Please copy export.zip to this directory.")

# Send data to Pixela, one pixel at a time.
# This can take a long time. It can be safely interrupted & resumed.
try:
	latest = pixela.get_latest()
	i = health.filter(latest) if latest else 0
	for date in sorted(health.data.keys()):
		i += 1
		percent = 100.0 * i / health.numdays
		print(f"\rSetting pixel {i:,} of {health.numdays:,} ({percent:.2f}%)", end="")
		pixela.set_pixel(date, health.data[date])
except KeyboardInterrupt:
	exit("\nAborted.")

url = pixela.get_url()
call(["open", url])
print("Done!")
print(url)
