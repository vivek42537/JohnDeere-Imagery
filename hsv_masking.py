import cv2
import numpy as np

"""
Surya Salem
salem9@purdue.edu
DMJohnDeere - Ackerman-Allen

"""

img = cv2.imread('C:\\Users\\surya\\Documents\\PURDUE\\Datamine\\John Deere\\Satellite Imagery\\Ackerman-Allen\\Ackerman_NAIP_Images\\Ackerman_NAIP_Images.RGB.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([25, 40, 150])
upper_green = np.array([95, 85, 200])

mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow("og", img)
cv2.imshow("mask", mask)
cv2.imshow("res", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
