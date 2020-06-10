from glob import glob
from PIL import Image
from math import floor
from numpy import median

image_list = []
i = 0
for x in glob('images/*.png'):
	image_list.append(Image.open(x))
	#image_list[i].show()
	#i += 1

newImage = Image.new('RGB', (image_list[0].width, image_list[0].height))

for x in range(newImage.width):
	for y in range(newImage.height):
		pixel_list = []
		for i in image_list:
			pixel_list.append(i.getpixel((x,y)))
		pixel_list.sort()

		median = floor((len(pixel_list) + 1)/2)

		newImage.putpixel((x,y), pixel_list[median])

			
newImage.show()