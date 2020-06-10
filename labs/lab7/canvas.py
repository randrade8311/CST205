from PIL import Image

canvas = Image.new('RGB', (800, 800), 'blue')
im = Image.open("images/image1.png")
im1 = Image.open("images/image2.jpg")
im2 = Image.open("images/image3.jpg")

def creatingCollage(image, target_x, y):
	for source_x in range(image.width):
		target_y = y
		for source_y in range(image.height):
			color = image.getpixel((source_x,source_y))
			canvas.putpixel((target_x, target_y), color)
			target_y += 1
		target_x += 1

creatingCollage(im, 60, 100)
creatingCollage(im1, 350, 40)
creatingCollage(im2, 60, 450)

canvas.save("images/canvas.jpg")

canvas.show()