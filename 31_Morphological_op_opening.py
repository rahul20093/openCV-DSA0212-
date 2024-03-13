import cv2
import numpy as np
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

resized_width = int(opening.shape[1] * 0.15)
resized_height = int(opening.shape[0] * 0.15) 
imgResized = cv2.resize(opening, (resized_width, resized_height))
cv2.imshow("opening",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
