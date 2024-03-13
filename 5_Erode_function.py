import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "C:/Users/Rahul/Pictures/wallpapers/oppie.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel , iterations = 10)
imgEroded = cv2.erode(imgDilation,kernel,iterations=2)


resized_width = int(imgEroded.shape[1] * 0.15)
resized_height = int(imgEroded.shape[0] * 0.15) 
imgResized = cv2.resize(imgEroded, (resized_width, resized_height))
cv2.imshow("Img Erosion",imgResized)
cv2.waitKey(0)
