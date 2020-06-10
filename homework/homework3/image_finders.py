from glob import glob
from PIL import Image, ImageOps

#creates image and name dictionary
def createDict():
    image_dict = {'name': [], 'image': []}
    for x in glob('images/*.jpg'):
        image_dict['image'].append(Image.open(x))
        image_dict['name'].append((glob(x)))
    return image_dict

#finds the image which closely matches the key that the user inputs
def imageFinder(key1, image_dict):
    i = 0
    for y in image_dict['name']:
        if key1 in y[0]:
            return (image_dict['image'][i])
        i += 1

#sepia tone function
def sepiaTone(image):
    width, height = image.size

    image2 = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            r, g, b, = image.getpixel((x,y))

            newR = int(0.393 * r + 0.769 * g + 0.189 * b)
            newG = int(0.349 * r + 0.686 * g + 0.168 * b)
            newB = int(0.272 * r + 0.534 * g + 0.131 * b)

            if newR > 255:
                newR = 255
            if newG > 255:
                newG = 255
            if newB > 255:
                newB = 255

            image2.putpixel((x,y), (newR, newG, newB))

    return image2

#converts into negative tone
def negativeTone(image):
    image_inverted = ImageOps.invert(image)
    return image_inverted

#converts into grayscale
def grayscaleTone(image):
    grayscale = image.convert('LA')
    return grayscale

#resizes the image (size can be anything)
def thumbnailTone(image):
    newImage = image
    newImage.thumbnail((300, 300))
    return newImage

#keys would be what they inputed
def findPictureData(keys, image_info):
     temp = ['id', 0]
     chumba = keys.split()
     for x in image_info:
          count = 0
          for y in chumba:
               if y in x['tags']:
                    #print(x['tags'],y)
                    count=count+1
          if count>temp[1]:
               temp[1]=count
               temp[0]=x['id']
          elif count == temp[1]:
               if x['id']>temp[0]:
                    temp[0]=x['id']
     return temp