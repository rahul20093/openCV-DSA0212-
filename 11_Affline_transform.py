import cv2
import numpy as np

img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")
rows,cols,_ = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))


resized_width = int(dst.shape[1] * 0.15)
resized_height = int(dst.shape[0] * 0.15) 
imgResized = cv2.resize(dst, (resized_width, resized_height))
cv2.imshow("Affline transform",imgResized)


cv2.waitKey(0)
cv2.destroyAllWindows()
