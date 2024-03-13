import cv2
import numpy as np

im_src = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")

pts_src = np.array([[141, 131], [480, 159], [493, 630],[64, 601]])

im_dst = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")

pts_dst = np.array([[318, 256],[534, 372],[316, 670],[73, 473]])

h, status = cv2.findHomography(pts_src, pts_dst)

im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))

resized_width = int(im_src.shape[1] * 0.15)
resized_height = int(im_src.shape[0] * 0.15) 
imgResized = cv2.resize(im_src, (resized_width, resized_height))
cv2.imshow("Source Image",imgResized)

resized_width = int(im_dst.shape[1] * 0.15)
resized_height = int(im_dst.shape[0] * 0.15) 
imgResized = cv2.resize(im_dst, (resized_width, resized_height))
cv2.imshow("Destination Image",imgResized)

resized_width = int(im_out.shape[1] * 0.15)
resized_height = int(im_out.shape[0] * 0.15) 
imgResized = cv2.resize(im_out, (resized_width, resized_height))
cv2.imshow("Warped Source Image",imgResized)
