from PIL import Image

fruit = Image.open("images/fruit.jpg")

width, height = fruit.size

maxi = 0
coordinate = []

for x in range(width):
	for y in range(height):
		red = fruit.getpixel((x,y))
		if (red[0] > maxi):
			maxi = red[0]
			coordinate = (x,y)

print(maxi)
print(coordinate)

fruit.show()