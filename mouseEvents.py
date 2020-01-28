import cv2
import numpy as np


# Print coordinates on left click and color channels on right click
def click_event(event, x, y, flags, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        str_xy = str(x) + ', ' + str(y)
        cv2.putText(img, str_xy, (x, y), font, .5, (255, 255, 0), 2)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        str_channels = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, str_channels, (x, y), font, .5, (0, 255, 255), 2)

    cv2.imshow('image', img)


def click_event_advanced(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), 3)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 2)
        cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)  # create black image
img = cv2.imread('img/stars.jpg')
cv2.imshow('image', img)

# cv2.setMouseCallback('image', click_event)

points = []
cv2.setMouseCallback('image', click_event_advanced)

cv2.waitKey(0)
cv2.destroyAllWindows()
