from PIL import Image
import pickle 

colordict = {"red" : [0, 0, 0, 0], "green": [0,0,0,0], "blue": [0,0,0,0]}
with open('image_matrix', 'rb') as pickle_file:
	data = pickle.load(pickle_file)


"""colorlist = [ (54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167),
			  (204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93), 
     		  (71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122), 
      		  (168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]"""
def addingtodict(color, binx):
	if(color == 0):
		colordict["red"][binx] += 1
	elif(color == 1):
		colordict["green"][binx] += 1
	elif(color == 2):
		colordict["blue"][binx] += 1

def sizecheck(channel, color):
	color = color
	if(channel >= 0 and channel <=63):
		addingtodict(color, 0)
	elif(channel >= 64 and channel <=127):
		addingtodict(color, 1)
	elif(channel >= 128 and channel <= 191):
		addingtodict(color, 2)
	elif(channel >= 192 and channel <= 255):
		addingtodict(color, 3)


def forloopschecking(list):
	for y in range(len(list)):
		for x in range(3):
			sizecheck(list[y][x][0], x)
			sizecheck(list[y][x][1], x)
			sizecheck(list[y][x][2], x)
			#print(list[y][x])

forloopschecking(data)

print(colordict)

for x in range(len(data)):
	for y in range(len(data)):
		num = (x,y)

print(data)

#print(data)
