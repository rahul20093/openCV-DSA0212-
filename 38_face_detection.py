import cv2
img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/face1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier("C:/Users/Rahul/Downloads/haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

resized_width = int(img.shape[1] * 0.15)
resized_height = int(img.shape[0] * 0.15) 
imgResized = cv2.resize(img, (resized_width, resized_height))
cv2.imshow("Faces Detected",imgResized)


cv2.waitKey(0)
cv2.destroyAllWindows()
