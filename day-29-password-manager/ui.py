from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button
from tkinter import messagebox

class App:

	def __init__(self, db):

		# Save a reference to the database for later use.
		self.db = db

		# Set up program window.
		window = Tk()
		window.title('Password Manager')
		window.config(padx=20, pady=20)

		# Draw logo on a canvas.
		canvas = Canvas(width=200, height=200)
		logo_img = PhotoImage(file='logo.png')
		canvas.create_image(100, 100, image=logo_img)
		canvas.configure(background=self.db.bg_color())
		canvas.grid(row=0, column=0, columnspan=3)

		# Create entries and their labels.
		self.entries = {}
		for index, label in enumerate(['Website', 'Username', 'Password']):
			Label(text=f'{label}:').grid(row=index + 1, column=0, sticky='e')
			self.entries[label] = Entry(window, width=35 if label == 'Username' else 25)

		# Create input fields.
		self.entries['Website'].grid(row=1, column=1, columnspan=2, sticky='w')
		self.entries['Website'].focus()
		self.entries['Username'].grid(row=2, column=1, columnspan=2, sticky='w')
		self.entries['Username'].insert(0, db.default_username())
		self.entries['Password'].grid(row=3, column=1, sticky='w')

		# Create buttons.
		Button(text='Search', width=6, command=self.search).grid(row=1, column=2, sticky='e')
		Button(text='Generate', width=6, command=self.generate).grid(row=3, column=2, sticky='e')
		Button(text='Save', width=8, command=self.save).grid(row=4, column=0, columnspan=3)

		# Done setting up user interface.
		window.mainloop()

	def generate(self):
		self.entries['Password'].delete(0, 'end')
		self.entries['Password'].insert(0, self.db.generate())

	def save(self):
		self.db.save_record({label: e.get().strip() for label, e in self.entries.items()})

	def search(self):
		website = self.entries['Website'].get().strip()
		if len(website) < 1:
			messagebox.showerror(title='Error', message='Please enter a website.')
			return
		r = self.db.find_record(website)
		if r is None:
			messagebox.showerror(title='Error', message='Website not found in database.')
			return
		for label, entry in self.entries.items():
			entry.delete(0, 'end')
			entry.insert(0, r[label])
