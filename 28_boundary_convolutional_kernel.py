import cv2
import numpy as np
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg", cv2.IMREAD_GRAYSCALE)
dx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1)
edges = cv2.magnitude(dx, dy)
thresh = 100
edges[edges < thresh] = 0
edges[edges >= thresh] = 255

resized_width = int(edges.shape[1] * 0.15)
resized_height = int(edges.shape[0] * 0.15) 
imgResized = cv2.resize(edges, (resized_width, resized_height))
cv2.imshow("Edges",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
