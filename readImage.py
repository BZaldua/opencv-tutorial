import cv2

img = cv2.imread('img/stars.jpg', 0)  # read image in black and white
print(img)

cv2.imshow('image', img)  # open window and show the image
k = cv2.waitKey() & 0xFF  # get the key press

if k == 27:  # key ESC
    cv2.destroyAllWindows()  # close all windows opened
elif k == ord('s'):  # if S key pressed
    cv2.imwrite('img/output_stars_bw.png', img)  # save image w/ a new name
    cv2.destroyAllWindows()

