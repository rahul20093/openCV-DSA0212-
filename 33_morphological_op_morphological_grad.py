import cv2
import numpy as np
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

resized_width = int(grad.shape[1] * 0.15)
resized_height = int(grad.shape[0] * 0.15) 
imgResized = cv2.resize(grad, (resized_width, resized_height))
cv2.imshow("Gradient",imgResized)

cv2.waitKey
