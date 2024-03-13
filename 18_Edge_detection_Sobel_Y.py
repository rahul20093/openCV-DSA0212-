import cv2
# Read the original image
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")
# Display original image

resized_width = int(img.shape[1] * 0.15)
resized_height = int(img.shape[0] * 0.15) 
imgResized = cv2.resize(img, (resized_width, resized_height))
cv2.imshow("Original Image",imgResized)

cv2.waitKey(0)
# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
# Sobel Edge Detection
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
# Display Sobel Edge Detection Images

resized_width = int(sobely.shape[1] * 0.15)
resized_height = int(sobely.shape[0] * 0.15) 
imgResized = cv2.resize(sobely, (resized_width, resized_height))
cv2.imshow("Sobel Y",imgResized)

cv2.waitKey(0)
