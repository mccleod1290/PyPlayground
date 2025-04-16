import cv2
import numpy as np

image_path = input("Enter image path: ")
factor = float(input("Enter color enhancement factor (0.0 to 2.0): "))

img = cv2.imread(image_path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv[:,:,1] = hsv[:,:,1] * factor
enhanced = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('Original', img)
cv2.imshow('Enhanced', enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows() 