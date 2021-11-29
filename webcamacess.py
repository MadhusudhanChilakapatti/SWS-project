import cv2
import time

# The duration in seconds of the video captured
capture_duration = 10

cap = cv2.VideoCapture(0)

start = time.time()
end = 0
while(end < capture_duration):
    elapse = time.time()
    end = int(elapse - start)
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('webcam',frame)
        cv2.waitKey(1)
    else:
        break

cap.release()
cv2.destroyAllWindows()












