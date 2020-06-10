class Color:
	"""docstring for Color"""
	def __init__(self, name, red, green, blue):
		#instance variables unique to each instance
		self.name = name
		self.red = red
		self.green = green
		self.blue = blue
	def luminosity(self):
		return ((red+green+blue)/3)
	def breakdown(self):
		str = "Breakdown of " + self.name + ":\n" + \
				"Color: (" + str(self.red) + "," + \
							str(self.green) + "," + \
							str(self.blue) + 
blue = Color("bloring blue", 0, 0, 255)
green = Color("normal green", 0, 255, 0)

print("Blue is type: ", type(blue))
print("Breakdown of blue", blue.name, 
	(blue.red, blue.green, blue.blue))
print("Boring Blue's luminosity" , blue.luminosity())

#print(isinstance(a, str))
#print(blue.name)
		