import cv2

image_path = input("Enter image path: ")

img = cv2.imread(image_path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('Original', img)
cv2.imshow('HSV', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows() 