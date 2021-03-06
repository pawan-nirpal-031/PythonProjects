import cv2

img = cv2.imread('Lane1-a.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("test image",gray)
cv2.waitKey(0)