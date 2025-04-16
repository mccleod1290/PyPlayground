import cv2

image_path = input("Enter image path: ")
x1 = int(input("Enter x1 coordinate: "))
y1 = int(input("Enter y1 coordinate: "))
x2 = int(input("Enter x2 coordinate: "))
y2 = int(input("Enter y2 coordinate: "))

img = cv2.imread(image_path)
cropped = img[y1:y2, x1:x2]

cv2.imshow('Original', img)
cv2.imshow('Cropped', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows() 