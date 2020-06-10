from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser

#use the web page you chose here:
site = "http://freesound.org"
html = urlopen(site)

"""with open("freesound.html", "r") as file:
    html = file.read();
"""
soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

featured_sound_html = soup.find(id="featured_sound")

title_block_html = featured_sound_html.find('div', {"class": "sound_title"})

title_html = title_block_html.find('a', {'class': 'title'})

title = title_html['title']
#print(featured_sound_html.prettify())

metadata_html = featured_sound_html.find('div', {"class": "metadata"})

mp3_html = metadata_html.find('a', {"class": "mp3_file"})

mp3 = site + mp3_html['href']

print(title)
print(mp3)

webbrowser.open(mp3)

#print(title_html.prettify())