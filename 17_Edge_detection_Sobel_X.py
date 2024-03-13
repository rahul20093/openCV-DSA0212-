import cv2
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")

resized_width = int(img.shape[1] * 0.15)
resized_height = int(img.shape[0] * 0.15) 
imgRes = cv2.resize(img, (resized_width, resized_height))
cv2.imshow('Original', imgRes)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
resized_width = int(sobelx.shape[1] * 0.15)
resized_height = int(sobelx.shape[0] * 0.15) 
imgResized = cv2.resize(sobelx, (resized_width, resized_height))
cv2.imshow("Sobel X",imgResized)
cv2.waitKey(0)
