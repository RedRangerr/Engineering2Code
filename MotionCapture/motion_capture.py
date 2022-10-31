# Physical Threapy Motion Capture Device script
#Engineering 4
#Siddhu Mohan 2022

import cv2, numpy as np

#Function for mouse clicks
def mouseClick(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv = frame_hsv[y,x]
        #print("The mouse was clicked at x= ", x, "y = ", y)
        print("Hue = ", hsv[0], "Sat = ", hsv[1], "Value = ", hsv[2])

cap = cv2.VideoCapture(0) #0 is webcam number
#104,104,185
c1_upper = [4, 180, 200]
c1_lower = [0, 100, 120]
c1_upper = np.array(c1_upper, dtype='uint8')
c1_lower = np.array(c1_lower, dtype='uint8')



cv2.namedWindow("Webcam")
cv2.namedWindow("Filter")
cv2.setMouseCallback("Webcam", mouseClick, param=None)
while True:
    ret, frame = cap.read()

    #convert image to hsv
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(frame_hsv,c1_lower, c1_upper)
    c1_filter = cv2.bitwise_or(frame, frame, mask = mask)
    cv2.imshow("Webcam", frame)
    cv2.imshow("Filter", c1_filter)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

