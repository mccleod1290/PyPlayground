import cv2
import numpy as np

image_path = input("Enter image path: ")
shear_factor = float(input("Enter y-axis shear factor: "))

img = cv2.imread(image_path)
rows, cols = img.shape[:2]
M = np.float32([[1, 0, 0], [shear_factor, 1, 0]])
sheared = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Sheared', sheared)
cv2.waitKey(0)
cv2.destroyAllWindows() 