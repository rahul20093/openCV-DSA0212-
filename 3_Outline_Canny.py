import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "C:/Users/Rahul/Pictures/wallpapers/oppie.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)

resized_width = int(imgCanny.shape[1] * 0.15)
resized_height = int(imgCanny.shape[0] * 0.15) 
imgResized = cv2.resize(imgCanny, (resized_width, resized_height))
cv2.imshow("Img Canny",imgResized)
cv2.waitKey(0)
