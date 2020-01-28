import cv2

# cap = cv2.VideoCapture(0)  # capture video from the main camera
cap = cv2.VideoCapture('vid/sw-sample.mp4')  # read from a video file

# OUTPUT
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('vid/output_sw-sample_bw.mp4', fourcc, 20.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()  # read frame
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # transform to gray
        cv2.imshow('frame', gray)  # show in a window

        if cv2.waitKey(1) & 0xFF == ord('q'):  # if 'q' key pressed, exit
            break
    else:
        break

cap.release()  # needed to release resources
#out.release()
cv2.destroyAllWindows()
