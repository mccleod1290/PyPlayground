import cv2
import numpy as np

image_path = input("Enter image path: ")
angle = float(input("Enter rotation angle in degrees: "))

img = cv2.imread(image_path)
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
rotated = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Rotated', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows() 