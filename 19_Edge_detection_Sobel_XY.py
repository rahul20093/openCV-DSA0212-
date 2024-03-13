import cv2
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")
# Display original image

resized_width = int(img.shape[1] * 0.15)
resized_height = int(img.shape[0] * 0.15) 
imgResized = cv2.resize(img, (resized_width, resized_height))
cv2.imshow("Original",imgResized)

cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

resized_width = int(sobelxy.shape[1] * 0.15)
resized_height = int(sobelxy.shape[0] * 0.15) 
imgResized = cv2.resize(sobelxy, (resized_width, resized_height))
cv2.imshow("Sobel X Y using Sobel() function",imgResized)
cv2.waitKey(0)
