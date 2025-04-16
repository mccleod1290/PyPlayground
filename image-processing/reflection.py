import cv2

image_path = input("Enter image path: ")
direction = input("Enter reflection direction (horizontal/vertical): ").lower()

img = cv2.imread(image_path)
if direction == "horizontal":
    reflected = cv2.flip(img, 1)
else:
    reflected = cv2.flip(img, 0)

cv2.imshow('Original', img)
cv2.imshow('Reflected', reflected)
cv2.waitKey(0)
cv2.destroyAllWindows() 