from flask import Flask, render_template

app = Flask(__name__)

li = {
 'days': ['sun', 'mon', 'tues'],
 'flavors': ['sweet', 'sour'],
 'colors': ['blue', 'green', 'brown']
}

@app.route('/hello')
def hello():
	return 'Hello World From Flask'

@app.route('/temp1')
def page2func():
	return render_template('templates1.html', list1 = li)