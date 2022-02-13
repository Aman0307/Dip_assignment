import cv2
import numpy as np

img = cv2.imread("C:\\Users\\amans\\Documents\\DIP\\Image Arithmetic\\image addition\\animal-g598af865d_640.png")
blue=img.copy()
blue[:, :, 1] = 0
blue[:, :, 2] = 0

cv2.imshow('blue', blue)
cv2.imwrite('blue.jpg', blue)
cv2.waitKey(0)
cv2.destroyAllWindows()