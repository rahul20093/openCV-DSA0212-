import cv2
import numpy as np
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0,1,0], [1,-8,1], [0,1,0]])
sharpened = cv2.filter2D(gray, -1, kernel)

resized_width = int(gray.shape[1] * 0.15)
resized_height = int(gray.shape[0] * 0.15) 
imgResized = cv2.resize(gray, (resized_width, resized_height))
cv2.imshow("Original",imgResized)

resized_width = int(sharpened.shape[1] * 0.15)
resized_height = int(sharpened.shape[0] * 0.15) 
imgResized = cv2.resize(sharpened, (resized_width, resized_height))
cv2.imshow("Sharpened",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
