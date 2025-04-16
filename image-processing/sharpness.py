import cv2
import numpy as np

image_path = input("Enter image path: ")
kernel_size = int(input("Enter kernel size (odd number): "))

img = cv2.imread(image_path)
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows() 