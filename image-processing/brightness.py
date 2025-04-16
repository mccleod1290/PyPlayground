import cv2
import numpy as np

image_path = input("Enter image path: ")
brightness = int(input("Enter brightness value (-255 to 255): "))

img = cv2.imread(image_path)
enhanced = cv2.add(img, np.array([brightness]))

cv2.imshow('Original', img)
cv2.imshow('Enhanced', enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows() 