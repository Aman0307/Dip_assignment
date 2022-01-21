# Assignment 1 : Convert image to grayscale without built-in function

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\amans\\Downloads\\WhatsApp Image 2021-07-17 at 17.47.55.jpeg")
print('Image Shape',np.shape(img))
print(type(img[0][0][0]))

(row, col) = img.shape[0:2]
cv2.imshow('Original', img)
cv2.waitKey(0)
gray = np.zeros([row, col], dtype=np.uint8)
for i in range(0,row):
    for j in range(0, col):
        s = 0
        for k in range(0,3):
            s += img[i][j][k]
        gray[i][j] = s/3

cv2.imshow('Grayscale', gray)
cv2.waitKey(0)        
cv2.imwrite("gray.png",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
