from PIL import Image

le = Image.open('images/cow.jpg')

le.show()

print(le.histogram())

#print(type(le))

#print(dir(le))