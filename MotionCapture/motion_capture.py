# Physical Threapy Motion Capture Device script
#Engineering 4
#Siddhu Mohan 2022

import cv2, numpy as np




cap = cv2.VideoCapture(0) #0 is webcam number
#104,104,185
c1_upper = [185+50, 104+50, 104+50]
c1_lower = [185 - 50, 104-50, 104-50]
c1_upper = np.array(c1_upper, dtype='uint8')
c1_lower = np.array(c1_lower, dtype='uint8')



cv2.namedWindow("Webcam")
while True:
    ret, frame = cap.read()

    mask = cv2.inRange(frame,c1_lower, c1_upper)
    c1_filter = cv2.bitwise_or(frame, frame, mask = mask)
    cv2.imshow("Webcam", c1_filter)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

