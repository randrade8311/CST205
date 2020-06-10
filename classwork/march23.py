import numpy as np
import cv2

# convert image to grayscale
im_gray = cv2.imread('../labs/lab13/images/march17.jpg', cv2.IMREAD_GRAYSCALE)

#
img2 = cv2.applyColorMap(im_gray, cv2.COLORMAP_HOT)

# use highgui to display image
cv2.imshow("MARCH 23", img2)

# keeps the image displayed
cv2.waitKey()