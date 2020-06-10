import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,QHBoxLayout,QComboBox
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtCore import pyqtSlot
my_list=['red','blue','green','yellow','black']
dic = {
'red':[(255,0,0),'#FF0000'],
'blue':[(0,0,255),'#0000FF'],
'green':[(0,255,0),'#00FF00'],
'yellow':[(255,255,0),'FFFF00'],
'black':[(0,0,0),'#000000']
}
class colorWideget(QWidget):
	def __init__(self):
		super().__init__()
		
		
	
	def setColor(self,color):
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QColor(color[0],color[1],color[2]))
		self.setPalette(p) 

class MainWidget(QWidget):
	"""docstring for MainWidget"""
	def __init__(self):
		super().__init__()
		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), QColor(0,0,0))
		self.setPalette(p) 
		
		self.setWindowTitle('Colors')
		self.label1 = QLabel('<font color="white">CST 205 Color Exchange</font>', self)
		self.label2 = QLabel('<font color="white">RGB: </font>', self)
		self.label3 = QLabel('<font color="white">HEX: </font>', self)

		self.my_combo_box = QComboBox()
		self.my_combo_box.addItems(my_list)
		self.my_label = QLabel("")

		self.btn = QPushButton("See Color!", self)
		self.btn.clicked.connect(self.newWindow) 

		vbox = QVBoxLayout()
		vbox.addWidget(self.label1)
		vbox.addWidget(self.my_combo_box)
		vbox.addWidget(self.label2)
		vbox.addWidget(self.label3)
		vbox.addWidget(self.my_label)
		vbox.addWidget(self.btn)

		self.setLayout(vbox)
		self.my_combo_box.currentIndexChanged.connect(self.update_ui)
		self.second = colorWideget()

	@pyqtSlot()
	def update_ui(self):
		my_index=self.my_combo_box.currentIndex()
		self.label2.setText(f'<font color="white">RGB: {dic[my_list[my_index]][0]}</font>')
		self.label3.setText(f'<font color="white">HEX: {dic[my_list[my_index]][1]}</font>')

	def newWindow(self):
		my_index=self.my_combo_box.currentIndex()
		self.second.setColor(dic[my_list[my_index]][0])
		self.second.show()


app = QApplication(sys.argv)
main = MainWidget()
main.show()
sys.exit(app.exec_())