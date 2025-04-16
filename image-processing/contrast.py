import cv2
import numpy as np

image_path = input("Enter image path: ")
contrast = float(input("Enter contrast value (0.0 to 3.0): "))

img = cv2.imread(image_path)
enhanced = cv2.convertScaleAbs(img, alpha=contrast, beta=0)

cv2.imshow('Original', img)
cv2.imshow('Enhanced', enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows() 