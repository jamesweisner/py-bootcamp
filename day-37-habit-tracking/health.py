from xml.etree.ElementTree import fromstring
from json import load, dump
from zipfile import ZipFile

class Health:

	def __init__(self, zipfile):
		self.zipfile = zipfile
		self.stepsfile = None
		self.numdays = 0
		self.data = None

	def extract(self, stepsfile):
		self.stepsfile = stepsfile
		try:
			with open(self.stepsfile) as file:
				print("Loading step totals...")
				self.data = load(file)
		except FileNotFoundError:
			self.data = {}
			print("Extracting raw step data...")
			with ZipFile(self.zipfile) as zip_file:
				with zip_file.open("apple_health_export/export.xml") as xml_file:
					root = fromstring(xml_file.read())
					for record in root.findall("Record"):
						if record.get("type") == "HKQuantityTypeIdentifierStepCount":
							date = record.get("startDate").split(" ")[0].replace('-', '')
							value = int(record.get("value"))
							if not date in self.data:
								self.data[date] = 0
							self.data[date] += value
			print("Saving daily step totals...")
			with open(self.stepsfile, 'w') as file:
				dump(self.data, file)

	def filter(self, latest):
		self.numdays = len(self.data)
		finished = [d for d in self.data.keys() if d < latest]
		for date in finished:
			del self.data[date]
		return len(finished)
