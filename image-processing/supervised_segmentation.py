import cv2
import numpy as np

image_path = input("Enter image path: ")
lower = np.array([0, 0, 0])
upper = np.array([255, 255, 255])

img = cv2.imread(image_path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Original', img)
cv2.imshow('Segmented', result)
cv2.waitKey(0)
cv2.destroyAllWindows() 