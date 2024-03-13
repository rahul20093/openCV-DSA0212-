import cv2
import numpy as np
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)

resized_width = int(dilation.shape[1] * 0.15)
resized_height = int(dilation.shape[0] * 0.15) 
imgResized = cv2.resize(dilation, (resized_width, resized_height))
cv2.imshow("Dilation",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
