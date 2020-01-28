import cv2

img = cv2.imread('img/stars.jpg', 1)

img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 2)  # draw a line. Image, origin, destiny, color, thikness
img = cv2.rectangle(img, (750, 750), (900, 850), (255, 0, 0), 3)  # draw a rectangle. origing -> top left, destiny -> bottom right
img = cv2.circle(img, (600, 600), 63, (0, 255, 0), 5)  # draw a circle

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Text test', (800, 400), font, 4, (150, 60, 200), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)  # wait for any key press to close windows
cv2.destroyAllWindows()