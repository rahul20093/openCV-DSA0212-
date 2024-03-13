import cv2
path ="C:/Users/Rahul/Pictures/wallpapers/oppie.jpg"
src = cv2.imread(path)
image = cv2.rotate(src, cv2.ROTATE_180)

resized_width = int(image.shape[1] * 0.15)
resized_height = int(image.shape[0] * 0.15) 
imgResized = cv2.resize(image, (resized_width, resized_height))
cv2.imshow("Image",imgResized)
cv2.waitKey(0)
