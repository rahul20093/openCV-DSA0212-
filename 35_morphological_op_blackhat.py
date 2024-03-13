import cv2
import numpy as np
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


resized_width = int(blackhat.shape[1] * 0.15)
resized_height = int(blackhat.shape[0] * 0.15) 
imgResized = cv2.resize(blackhat, (resized_width, resized_height))
cv2.imshow("Black Hat",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
