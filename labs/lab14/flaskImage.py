from flask import Flask, flash, redirect, render_template, request, url_for
import cv2
from opencv import getTodaysImage, modifyImage, getDatesDict
import datetime

app = Flask(__name__)

colors = {'Autumn': cv2.COLORMAP_AUTUMN, 'Bone': cv2.COLORMAP_BONE, 'Jet': cv2.COLORMAP_JET,
          'Winter': cv2.COLORMAP_WINTER, 'Rainbow': cv2.COLORMAP_RAINBOW, 'Ocean': cv2.COLORMAP_OCEAN,
          'Summer': cv2.COLORMAP_SUMMER, 'Spring': cv2.COLORMAP_SPRING, 'Cool' : cv2.COLORMAP_COOL,
          'HSV': cv2.COLORMAP_HSV, 'Pink' : cv2.COLORMAP_PINK, 'Hot' : cv2.COLORMAP_HOT}

          
@app.route('/', methods=['GET', 'POST'])
def home():
    image = getTodaysImage()
    date = datetime.date.today()
    image_dict = getDatesDict()
    return render_template(
        'image.html',
        data=colors, img = image, today = date, images = image_dict)

@app.route("/image" , methods=['GET', 'POST'])
def image():
    select = request.form.get('comp_select')
    imgDate = request.form.get('image_select')
    image = modifyImage(colors[select], select, imgDate)
    return render_template('newImage.html', img = image, date = imgDate, selected = select) # just to see what select is

if __name__=='__main__':
    app.run(debug=True)