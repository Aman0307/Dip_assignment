# Histogram Equalization without using built-in function
from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread("C:\\Users\\amans\\Documents\\DIP\\Image Arithmetic\\image addition\\animal-g598af865d_640.png",0)
plt.hist(img)
plt.xlabel('pixel')
plt.ylabel('frequency')
plt.savefig("gray_histogram.png")

a = np.zeros((256,),dtype=np.float16)
b = np.zeros((256,),dtype=np.float16)

height,width=img.shape

#finding histogram
for i in range(width):
    for j in range(height):
        g = img[j,i]
        a[g] = a[g]+1

print(a)   


#performing histogram equalization
tmp = 1.0/(height*width)
b = np.zeros((256,),dtype=np.float16)

for i in range(256):
    for j in range(i+1):
        b[i] += a[j] * tmp
    b[i] = round(b[i] * 255)

# b now contains the equalized histogram
b=b.astype(np.uint8)

print(b)

#Re-map values from equalized histogram into the image
for i in range(width):
    for j in range(height):
        g = img[j,i]
        img[j,i]= b[g]

#pix,freq = np.unique(img, return_index=True)
cv2.imshow('equalized_gray', img)
cv2.imwrite('equalized_gray.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(img)
plt.xlabel('pixel')
plt.ylabel('frequency')
plt.savefig("gray_eq_histogram.png")