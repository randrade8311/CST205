from PIL import Image
im = Image.open('monalisa2.jpg')

def negative_image(pixel):
	return (lambda a : 255 - a, pixel)
negative_list = map(negative_image, im.getdata() )
im.putdata(list(negative_list))
im.show()