import cv2
import numpy as np

image_path = input("Enter image path: ")
tx = int(input("Enter x translation value: "))
ty = int(input("Enter y translation value: "))

img = cv2.imread(image_path)
rows, cols = img.shape[:2]
M = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Translated', translated)
cv2.waitKey(0)
cv2.destroyAllWindows() 