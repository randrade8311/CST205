from PIL import Image
def changePicture():
	a = input('Insert image path.')
	sunset = Image.open(a)
	value = input(float('How would you like to edit your GB values?'))
	new_list = map(lambda a : (a[0], int(a[1]* value)), int(a[2]* value), sunset.getdata())
	sunset.putdata(list(new_list))
	sunset.show()	
while True:
	changePicture()
	ans = input("Would you like to continue? (q to quit")
	if(ans == 'q'):
		break