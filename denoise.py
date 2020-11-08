import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

"""
Vivek Khanolkar
vkhanolk@purdue.edu
Ackerman Allen team - John Deere
"""

path = "/Users/vivek/Documents/CÖDĘ/DataMine-John/hsvImage.jpg" #This is the res image from Surya's HSV mask
# print(os.path.exists(path))
img = cv.imread(os.path.abspath(path))
# print("IMAGE:", img)

dst = cv.fastNlMeansDenoisingColored(img,None,80,80,15,45) #10,10,7,21
# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
#plt.imshow(img)
plt.imshow(dst)
plt.show()