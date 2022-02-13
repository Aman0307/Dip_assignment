import cv2
import numpy as np

img = cv2.imread("C:\\Users\\amans\\Documents\\DIP\\Image Arithmetic\\image addition\\animal-g598af865d_640.png")
green=img.copy()
green[:, :, 0] = 0
green[:, :, 2] = 0

cv2.imshow('green', green)
cv2.imwrite('green.jpg', green)
cv2.waitKey(0)
cv2.destroyAllWindows()