import cv2
import numpy as np
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


resized_width = int(closing.shape[1] * 0.15)
resized_height = int(closing.shape[0] * 0.15) 
imgResized = cv2.resize(closing, (resized_width, resized_height))
cv2.imshow("Closing",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
