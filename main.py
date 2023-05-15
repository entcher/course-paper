import cv2

img = cv2.imread('image.png')  
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade = cv2.CascadeClassifier('cascade/cascade.xml')  
detections = haar_cascade.detectMultiScale(gray_img)
  
for (x, y, w, h) in detections:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
  
cv2.imshow('Detected objects', img)  
cv2.waitKey(0)
