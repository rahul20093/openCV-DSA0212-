import cv2
import numpy as np
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

resized_width = int(erosion.shape[1] * 0.15)
resized_height = int(erosion.shape[0] * 0.15) 
imgResized = cv2.resize(erosion, (resized_width, resized_height))
cv2.imshow("Erosion",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
