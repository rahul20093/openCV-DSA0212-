import cv2
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")
cv2.imshow('Original', img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
resized_width = int(edges.shape[1] * 0.15)
resized_height = int(edges.shape[0] * 0.15) 
imgResized = cv2.resize(edges, (resized_width, resized_height))
cv2.imshow("Canny Edge Detection",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
