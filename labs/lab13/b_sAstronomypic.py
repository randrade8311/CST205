from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser
from PIL import Image
from glob import glob

#web page of choosing
site = "https://apod.nasa.gov/apod/astropix.html"
html = urlopen(site)

soup = BeautifulSoup(html, 'html.parser')

cosmos_body = soup.find('body')

cosmos_first_center_tag = cosmos_body.find('center')

image = cosmos_first_center_tag.find('iframe')['src']

print(image)

webbrowser.open(image)

#cosmos_img = cosmos_first_center_tag.find('a')[1]

#mp3 = site + cosmos_img['href']

#print(mp3)

#webbrowser.open(image)

#cosmos_img = cosmos_first_center_tag.find_all('a')[1]['href']

#webbrowser.open(cosmos_img)

#cosmos_img.show()

#print(cosmos_img)