import cv2
import numpy as np

image_path = input("Enter image path: ")
operation = input("Enter operation (erosion/dilation): ").lower()
kernel_size = int(input("Enter kernel size: "))

img = cv2.imread(image_path, 0)
kernel = np.ones((kernel_size, kernel_size), np.uint8)

if operation == "erosion":
    result = cv2.erode(img, kernel, iterations=1)
else:
    result = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Original', img)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows() 