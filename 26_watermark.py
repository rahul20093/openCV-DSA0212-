import cv2
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")
wm = cv2.imread("C:/Users/Rahul/Downloads/logo.png")
h_wm, w_wm = wm.shape[:2]
h_img, w_img = img.shape[:2]
center_x = int(w_img/2)
center_y = int(h_img/2)
top_y = center_y - int(h_wm/2)
left_x = center_x - int(w_wm/2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm
roi = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi, 1, wm, 0.3, 0)
img[top_y:bottom_y, left_x:right_x] = result

resized_width = int(img.shape[1] * 0.15)
resized_height = int(img.shape[0] * 0.15) 
imgResized = cv2.resize(img, (resized_width, resized_height))
cv2.imshow("Watermarked Image",imgResized)

cv2.waitKey(0)
cv2.destroyAllWindows()
