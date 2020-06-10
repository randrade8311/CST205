#
# my_gui
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 25 February 2020
# 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel,QComboBox ,QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtCore import pyqtSlot
from image_finders import createDict, imageFinder, sepiaTone, negativeTone, grayscaleTone, thumbnailTone, findPictureData

# list for dropdown menu
my_list=['none','sepia','negative','grayscale','thumbnail']
	
class MainWidget(QWidget):
	"""Main window that dispalys widgets """
	def __init__(self):
		super().__init__()
		self.setStyleSheet("QLabel{ color: white; margin:none; text-align:center;}");
		# Background color declaration
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QColor(0,0,0))
		self.setPalette(p) 
		
		# Label Declarations
		self.setWindowTitle('Image Search')
		self.label1 = QLabel('      Welcome to Rodrigo & Nicolas\'s Enhanced Image Search', self)
		self.line = QLineEdit(self)
		self.filterLabel = QLabel('Filter:')
		self.tagLabel = QLabel('Tags:')

		self.my_combo_box = QComboBox()
		self.my_combo_box.addItems(my_list)
		

		# Button that opens window with current color as the background
		self.btn = QPushButton("Go!", self)
		self.btn.clicked.connect(self.newWindow) 

		# Widgets added layouts
		vbox = QVBoxLayout()
		hbox = QHBoxLayout()
		mbox = QVBoxLayout()

		vbox.addWidget(self.label1)

		hbox.addWidget(self.filterLabel)
		hbox.addWidget(self.my_combo_box)
		hbox.addWidget(self.tagLabel)
		hbox.addWidget(self.line)

		mbox.addLayout(vbox)
		mbox.addLayout(hbox)
		mbox.addWidget(self.btn)

		self.setLayout(mbox)

	@pyqtSlot()
	def newWindow(self):
		"""opens new window with the current color index as the background"""
		filter_index=self.my_combo_box.currentIndex()
		text_boi= self.line.text()

		#finds the picture with the most keys equaled
		id = findPictureData(text_boi, image_info)

		#gets the dictionary from the (image_finders.py) file
		image_dict = createDict()

		#passes in the id from the most relevant picture along with the dictionary
		image = imageFinder(id[0], image_dict)

		# sets approprate filter
		if my_list[filter_index] == 'sepia':
			image = sepiaTone(image)
		elif(my_list[filter_index] == 'negative'):
		#changes the picture into negative tone
			image = negativeTone(image)
		elif(my_list[filter_index] == 'grayscale'):
		#changes the picture into grayscale tone
			image = grayscaleTone(image)
		elif(my_list[filter_index] == 'thumbnail'):
			image = thumbnailTone(image)

		image.show()

image_info = [
     {
           "id" : "34694102243_3370955cf9_z",
           "title" : "Eastern",
           "flickr_user" : "Sean Davis",
           "tags" : ["Los Angeles", "California", "building"]
      },
      {
           "id" : "37198655640_b64940bd52_z",
           "title" : "Spreetunnel",
           "flickr_user" : "Jens-Olaf Walter",
           "tags" : ["Berlin", "Germany", "tunnel", "ceiling"]
      },
      {
           "id" : "36909037971_884bd535b1_z",
           "title" : "East Side Gallery",
           "flickr_user" : "Pieter van der Velden",
           "tags" : ["Berlin", "wall", "mosaic", "sky", "clouds"]
      },
      {
           "id" : "36604481574_c9f5817172_z",
           "title" : "Lombardia, september 2017",
           "flickr_user" : "Mónica Pinheiro",
           "tags" : ["Italy", "Lombardia", "alley", "building", "wall"]
      },
      {
           "id" : "36885467710_124f3d1e5d_z",
           "title" : "Palazzo Madama",
           "flickr_user" : "Kevin Kimtis",
           "tags" : [ "Rome", "Italy", "window", "road", "building"]
      },
      {
           "id" : "37246779151_f26641d17f_z",
           "title" : "Rijksmuseum library",
           "flickr_user" : "John Keogh",
           "tags" : ["Amsterdam", "Netherlands", "book", "library", "museum"]
      },
      {
           "id" : "36523127054_763afc5ed0_z",
           "title" : "Canoeing in Amsterdam",
           "flickr_user" : "bdodane",
           "tags" : ["Amsterdam", "Netherlands", "canal", "boat"]
      },
      {
           "id" : "35889114281_85553fed76_z",
           "title" : "Quiet at dawn, Cabo San Lucas",
           "flickr_user" : "Erin Johnson",
           "tags" : ["Mexico", "Cabo", "beach", "cactus", "sunrise"]
      },
      {
           "id" : "34944112220_de5c2684e7_z",
           "title" : "View from our rental",
           "flickr_user" : "Doug Finney",
           "tags" : ["Mexico", "ocean", "beach", "palm"]
      },
      {
           "id" : "36140096743_df8ef41874_z",
           "title" : "Someday",
           "flickr_user" : "Thomas Hawk",
           "tags" : ["Los Angeles", "Hollywood", "California", "Volkswagen", "Beatle", "car"]
      }
]
		


app = QApplication(sys.argv)
main = MainWidget()
main.show()
sys.exit(app.exec_())