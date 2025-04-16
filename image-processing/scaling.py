import cv2

image_path = input("Enter image path: ")
scale_x = float(input("Enter x scaling factor: "))
scale_y = float(input("Enter y scaling factor: "))

img = cv2.imread(image_path)
scaled = cv2.resize(img, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)

cv2.imshow('Original', img)
cv2.imshow('Scaled', scaled)
cv2.waitKey(0)
cv2.destroyAllWindows() 