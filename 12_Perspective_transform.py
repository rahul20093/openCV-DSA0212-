import cv2
import numpy as np
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[100,50],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(cols, rows))

resized_width = int(dst.shape[1] * 0.15)
resized_height = int(dst.shape[0] * 0.15) 
imgResized = cv2.resize(dst, (resized_width, resized_height))
cv2.imshow("Transformed Image",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
