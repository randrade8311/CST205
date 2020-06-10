#imported libraries
from bs4 import BeautifulSoup
import requests
import webbrowser
import numpy as np
import cv2

"""Created by: Rodrigo Andrade && Nicolas Lara
This code opens up the website inputed,
then it looks where the image is placed
and grabs the image. Then it opens it in a browser
This is also an updating website so 
everyday it will open a different image"""

#web page of choosing
site = requests.get("https://www.smithsonianmag.com/category/photo-of-the-day/").text
#print(site.text)
#uses BeautifulSoup
soup = BeautifulSoup(site, 'html.parser')
#finds the class 'day-feature' within the 'aside' tag
image_place = soup.find('aside', {'class': 'day-feature'})
#finds the image itself within 'image_place'
image = image_place.find('img')['src']
#opens the link in the local browser
#webbrowser.open(image)
#prints the image URL
img = requests.get(image, stream=True).raw

new_img = np.asarray(bytearray(img.read()), dtype="uint8")
new_img = cv2.imdecode(new_img, cv2.IMREAD_COLOR)

cv2.imshow('title', new_img)

cv2.waitKey(0)
#print(type(img))
#print(new_img)
