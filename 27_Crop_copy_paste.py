import cv2
import numpy as np
image = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")
img2 = cv2.imread("C:/Users/Rahul/Downloads/logo.png")
print(image.shape) # Print image shape

resized_width = int(image.shape[1] * 0.15)
resized_height = int(image.shape[0] * 0.15) 
imgResized = cv2.resize(image, (resized_width, resized_height))
cv2.imshow("original",imgResized)


imageCopy = image.copy()
cv2.circle(imageCopy, (100, 100), 30, (255, 0, 0), -1)

resized_width = int(image.shape[1] * 0.15)
resized_height = int(image.shape[0] * 0.15) 
imgResized = cv2.resize(image, (resized_width, resized_height))
cv2.imshow("image",imgResized)

resized_width = int(imageCopy.shape[1] * 0.15)
resized_height = int(imageCopy.shape[0] * 0.15) 
imgResized = cv2.resize(imageCopy, (resized_width, resized_height))
cv2.imshow("image copy",imgResized)

cropped_image = image[80:280, 150:330]

resized_width = int(cropped_image.shape[1] * 0.15)
resized_height = int(cropped_image.shape[0] * 0.15) 
imgResized = cv2.resize(cropped_image, (resized_width, resized_height))
cv2.imshow("cropped",imgResized)

cv2.imwrite("Cropped Image.jpg", cropped_image)
dst = cv2.addWeighted(image, 0.5, img2, 0.7, 0)
img_arr = np.hstack((image, img2))

resized_width = int(img_arr.shape[1] * 0.15)
resized_height = int(img_arr.shape[0] * 0.15) 
imgResized = cv2.resize(img_arr, (resized_width, resized_height))
cv2.imshow("Input Images",imgResized)

resized_width = int(dst.shape[1] * 0.15)
resized_height = int(dst.shape[0] * 0.15) 
imgResized = cv2.resize(dst, (resized_width, resized_height))
cv2.imshow("Blended Image",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
