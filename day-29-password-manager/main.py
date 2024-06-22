from getpass import getpass
from db import Database
from ui import App

db = Database(getpass('Enter password: '))

app = App(db)
