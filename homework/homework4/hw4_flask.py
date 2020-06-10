from flask import Flask, flash, redirect, render_template, request, url_for
from image_info import image_info
from random import sample
from PIL import Image
from glob import glob

app = Flask(__name__)

@app.route('/')
def home():
    list1 = [0,1,2,3,4,5,6,7,8,9]
    n = sample(list1, 3)
    return render_template("home.html", img1 = image_info[n[0]], img2 = image_info[n[1]], img3= image_info[n[2]])

@app.route('/picture/<id>')
def display(id):
    for i in image_info:
        if id == i['id']:
            img = i
    name = (f'static/{id}.jpg')
    im = Image.open(name)
    width, height = im.size
    form = im.format
    mo = im.mode
    return render_template("picture.html", i = img, w = width, h = height, f = form, m = mo)

if __name__=='__main__':
    app.run(debug=True)