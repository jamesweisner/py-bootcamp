from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import get
from game import Game

# Download HTML from the source website.
response = get('https://www.ipl.org/div/stateknow/chart.html')
assert response.status_code == 200

# Parse the HTML and find the <table> with our data in it.
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='sk_charttable')
assert table is not None
assert isinstance(table, Tag)

# Load the original CSV provided to students.
game = Game('states-v1.csv')
game.states.insert(2, 'capital', None)
game.states.insert(3, 'bird', None)
game.states.insert(4, 'flower', None)

# Import State capital, bird, and flower.
for row in table.find_all('tr'):
    cells = [c.text.strip() for c in row.find_all(['td'])]
    if len(cells) < 4:
        continue  # Header row.
    name = cells[0]
    if not name in game.states.index:
        continue
    for column, index in [('capital', 1), ('bird', 3), ('flower', 4)]:
        game.states.at[name, column] = cells[index]

# Save these changes to a new file.
game.save('states-v2.csv')
