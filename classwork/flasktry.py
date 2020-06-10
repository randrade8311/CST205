from flask import Flask, flash, redirect, render_template, request, url_for
from opencv import getImage

app = Flask(__name__)

colors = {'Autumn': 'COLORMAP_AUTUMN', 'Bone': 'COLORMAP_BONE', 'Jet': 'COLORMAP_JET',
          'Winter': 'COLORMAP_WINTER', 'Rainbow': 'COLORMAP_RAINBOW', 'Ocean': 'COLORMAP_OCEAN',
          'Summer': 'COLORMAP_SUMMER', 'Spring': 'COLORMAP_SPRING', 'Cool' : 'COLORMAP_COOL',
          'HSV': 'COLORMAP_HSV', 'Pink' : 'COLORMAP_PINK', 'Hot' : 'COLORMAP_HOT'}

@app.route('/')
def home():
    return render_template(
        'index.html',
        data=colors, image = getImage())

@app.route("/image" , methods=['GET', 'POST'])
def image():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is

if __name__=='__main__':
    app.run(debug=True)