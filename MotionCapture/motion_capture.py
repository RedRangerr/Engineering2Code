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
blue_upper = [107, 255, 200]
blue_lower = [99, 117, 50]


#blue azores
blue_upper = np.array(blue_upper, dtype='uint8')
blue_lower = np.array(blue_lower, dtype='uint8')
#diva glam
pink_upper = np.array([177, 200, 180 ], dtype='uint8')
pink_lower = np.array([167, 100, 120], dtype='uint8')
#Violet Obsession
purple_upper = np.array([137, 100, 130 ], dtype='uint8')
purple_lower = np.array([124, 25, 80 ], dtype='uint8')

cv2.namedWindow("Webcam")
cv2.namedWindow("Filter")
cv2.setMouseCallback("Webcam", mouseClick, param=None)
kernel = np.ones((5,5), np.uint8)
while True:
    ret, frame = cap.read()

    #convert image to hsv
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #create blue mask
    blue_mask = cv2.inRange(frame_hsv,blue_lower, blue_upper)
    blue_mask = cv2.erode(blue_mask, kernel, iterations=1)
    blue_filter = cv2.bitwise_or(frame, frame, mask = blue_mask)

    #create pink mask
    pink_mask = cv2.inRange(frame_hsv, pink_lower, pink_upper)
    pink_mask = cv2.erode(pink_mask, kernel, iterations=1)
    pink_filter = cv2.bitwise_or(frame, frame, mask=pink_mask)

    #create purple filter
    purple_mask = cv2.inRange(frame_hsv, purple_lower, purple_upper)
    purple_mask = cv2.erode(purple_mask, kernel, iterations=1)
    purple_filter = cv2.bitwise_or(frame, frame, mask=purple_mask)

    #create filtered image
    filtered_image = cv2.bitwise_or(blue_filter, pink_filter)
    filtered_image = cv2.bitwise_or(filtered_image, purple_filter)

    cv2.imshow("Webcam", frame)
    cv2.imshow("Filter", filtered_image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

