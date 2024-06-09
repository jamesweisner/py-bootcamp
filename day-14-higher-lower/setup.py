from json import dumps

from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import get

URL = 'https://us.youtubers.me/global/all/top-1000-most-subscribed-youtube-channels'

# Download HTML from the source website.
response = get(URL)
assert response.status_code == 200
response.encoding = response.apparent_encoding
assert response.encoding.lower() == 'utf-8'

# Parse the HTML and find the <table> with our data in it.
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='top-charts')
assert table is not None
assert isinstance(table, Tag)

# Generate a list of the top 1,000 YouTube channels.
channels = []
for row in table.find_all('tr'):
    cells = row.find_all(['td'])
    if len(cells) < 1:
        continue  # Header row.
    channels.append({
        'name': cells[1].text.strip(),
        'subs': int(cells[2].text.strip().replace(',', '')),
        'type': cells[5].text.strip(),
        'year': int(cells[6].text.strip()),
    })

# Save channel data to a JSON file.
with open('channels.json', 'w', encoding='utf-8') as file:
    file.write(dumps(channels, indent=2))
