import cv2
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")
x, y = 100, 100
width, height = 500, 350
roi = img[y:y+height, x:x+width]

resized_width = int(roi.shape[1] * 2)
resized_height = int(roi.shape[0] * 2) 
imgResized = cv2.resize(roi, (resized_width, resized_height))
cv2.imshow("ROI",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
