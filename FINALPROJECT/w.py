import cv2
import datetime
from test import ITT

date = datetime.date.today()

camera_port = 0
camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
return_value, image = camera.read()
cv2.imwrite(f"image{date}.png", image)

name = f"image{date}.png"

camera.release()

i = ITT(name)
print(i.imageToText())
print(i.imageToSpeech())

cv2.imshow('show', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
