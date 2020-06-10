import math
from PIL import Image
from colormath import color_diff_matrix
import numpy


def _get_lab_color1_vector(color):
    """
    Converts an LabColor into a NumPy vector.

    :param LabColor color:
    :rtype: numpy.ndarray
    """
    if not color.__class__.__name__ == 'LabColor':
        raise ValueError(
            "Delta E functions can only be used with two LabColor objects.")
    return numpy.array([color.lab_l, color.lab_a, color.lab_b])

def _get_lab_color2_matrix(color):
    """
    Converts an LabColor into a NumPy matrix.

    :param LabColor color:
    :rtype: numpy.ndarray
    """
    if not color.__class__.__name__ == 'LabColor':
        raise ValueError(
            "Delta E functions can only be used with two LabColor objects.")
    return numpy.array([(color.lab_l, color.lab_a, color.lab_b)])


def delta_e_cie2000(color1, color2, Kl=1, Kc=1, Kh=1):
    """
    Calculates the Delta E (CIE2000) of two colors.
    """
    color1_vector = _get_lab_color1_vector(color1)
    color2_matrix = _get_lab_color2_matrix(color2)
    delta_e = color_diff_matrix.delta_e_cie2000(
        color1_vector, color2_matrix, Kl=Kl, Kc=Kc, Kh=Kh)[0]
    return numpy.asscalar(delta_e)

def distance(color_1, color_2):
	red_diff = math.pow((color_1[0] - color_2[0]), 2)
	green_diff = math.pow((color_1[1] - color_2[1]), 2)
	blue_diff = math.pow((color_1[2] - color_2[2]), 2)
	return math.sqrt(red_diff + green_diff + blue_diff)
def chromakey(source, bg):
	for x in range(source.width):
		for y in range(source.height):
			cur_pixel = source.getpixel((x,y))
			green = (0, 190, 60)
			if delta_e_cie2000(cur_pixel, green, Kl=1,Kc=1,Kh=1) < 250:
 			# grab the color at the same spot from the new background
				source.putpixel((x,y), bg.getpixel((x,y)))
	source.save("images/chromakeyed.png")

building = Image.open("images/bit.jpg")
asteroid = Image.open("images/dinosaur.png")

chromakey(asteroid, building)
im = Image.open("images/chromakeyed.png")
im.show()