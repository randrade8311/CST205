#imported libraries
from bs4 import BeautifulSoup
import requests
import numpy as np
import cv2
import datetime
from glob import glob

"""Created by: Rodrigo Andrade && Nicolas Lara
This code opens up the website inputed,
then it looks where the image is placed
and grabs the image. Then it opens it in a browser
This is also an updating website so 
everyday it will open a different image"""

def getTodaysImage():
    site = requests.get("https://www.smithsonianmag.com/category/photo-of-the-day/").text
    soup = BeautifulSoup(site, 'html.parser')
    image_place = soup.find('aside', {'class': 'day-feature'})
    image = image_place.find('img')['src']
    img = requests.get(image, stream=True).raw
    new_img = np.asarray(bytearray(img.read()), dtype="uint8")
    new_img = cv2.imdecode(new_img, cv2.IMREAD_COLOR)
    date = datetime.date.today()
    cv2.imwrite(f"static/{date}Image.jpg", new_img)
    cv2.imwrite(f"original/{date}Image.jpg", new_img)
    return (f"{date}Image.jpg")

def modifyImage(newMap, key, imgDate):
    img_dict = getDatesDict()
    i = 0
    for x in img_dict['dates']:
        if imgDate in x:
            img = img_dict['images'][i]
        i += 1
    img = cv2.applyColorMap(img, newMap)
    cv2.imwrite(f"static/{imgDate}{key}.jpg", img)
    return (f'{imgDate}{key}.jpg')

def getDatesDict():
    dates_dict = {'dates': [], 'images': []}
    for x in glob('original/*.jpg'):
        dates_dict['images'].append(cv2.imread(x))
        name = glob(x)
        name = name[0].lstrip('original\\')
        name = name.replace('Image.jpg', ' ')
        dates_dict['dates'].append(name)
    return dates_dict
