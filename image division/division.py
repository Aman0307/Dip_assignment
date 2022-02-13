import cv2
import numpy as np

img = cv2.imread("C:\\Users\\amans\\Documents\\DIP\\Image Arithmetic\\image addition\\animal-g598af865d_640.png")
sum_pix = np.zeros([1101, 1500, 3], dtype=np.uint8)

print(np.shape(img))  
for i in range(0,640):
    for j in range(0,480):
        for k in range(0,3):
            sum_pix[i][j][k] = img[i][j][k]/3   # Division
cv2.imshow('division', sum_pix)
cv2.imwrite('division.png', sum_pix)        
cv2.waitKey(0)
cv2.destroyAllWindows()