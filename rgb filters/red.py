import cv2
import numpy as np

img = cv2.imread("C:\\Users\\amans\\Documents\\DIP\\Image Arithmetic\\image addition\\animal-g598af865d_640.png")
red=img.copy()
red[:, :, 0] = 0
red[:, :, 1] = 0
#red[1,:,:]=img[0,0,:]
cv2.imshow('red', red)
cv2.imwrite('red.jpg', red)
cv2.waitKey(0)
cv2.destroyAllWindows()