import numpy as np
import cv2

img = cv2.imread('img/stars.jpg')
img2 = cv2.imread('img/death-star.png')

print(img.shape)  # rows, columns and channels
print(img.size)  # pixels
print(img.dtype)  # datatype

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

img = cv2.resize(img, (1000, 800))
img2 = cv2.resize(img2, (1000, 800))

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .7, img2, .3, 0)  # kind of watermark

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()