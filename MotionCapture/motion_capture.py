# Physical Threapy Motion Capture Device script
#Engineering 4
#Siddhu Mohan 2022

import cv2, numpy as np
import math_helpers
import time
import csv
import os
import datetime
#Function for mouse clicks
def mouseClick(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv = frame_hsv[y,x]
        #print("The mouse was clicked at x= ", x, "y = ", y)
        print("Hue = ", hsv[0], "Sat = ", hsv[1], "Value = ", hsv[2])

def centroid_finder(input_image, output_image):
    moments = cv2.moments(input_image)

    if moments['m00'] == 0:
        centroid_x = 1
        centroid_y = 1
    else:
        centroid_x = moments["m10"]/moments["m00"]
        centroid_y = moments["m01"]/moments["m00"]
    
    cv2.circle(output_image, (int(centroid_x),int(centroid_y)), 5, (255,255,255), -1)
    return [int(centroid_x), int(centroid_y)]

cap = cv2.VideoCapture(0) #0 is webcam number
#color 1(blue)
c1_upper = np.array([106, 255, 220], dtype='uint8')
c1_lower = np.array([95, 110, 50], dtype='uint8')
#color 2(green)
c3_upper = np.array([170, 140, 240], dtype='uint8')
c3_lower = np.array([160, 50, 100], dtype='uint8')
#color 3(pink)
c2_upper = np.array([75, 190, 220], dtype='uint8')
c2_lower = np.array([67, 60, 70], dtype='uint8')
#color 4(pink)

#My colors
# c1_upper = np.array([74, 180, 150], dtype='uint8')
# c1_lower = np.array([60, 70, 70], dtype='uint8')

# c2_upper = np.array([106, 255, 160], dtype='uint8')
# c2_lower = np.array([95, 100, 100], dtype='uint8')

# c4_upper = np.array([176, 100, 255 ], dtype='uint8')
# c4_lower = np.array([167, 40, 100 ], dtype='uint8')

# c3_upper = np.array([33, 150, 255], dtype='uint8')
# c3_lower = np.array([30, 0, 100], dtype='uint8')
"""
c1_upper = np.array([99, 217, 255], dtype='uint8')
c1_lower = np.array([90, 60, 60], dtype='uint8')
#color 2(plymouth plumb)
c2_upper = np.array([179, 140, 255], dtype='uint8')
c2_lower = np.array([173, 55, 70], dtype='uint8')
#color 3(dutch tulip)
c3_upper = np.array([28, 150, 255], dtype='uint8')
c3_lower = np.array([22, 40, 160], dtype='uint8')
#color 4(green)
c4_upper = np.array([62, 150, 175], dtype='uint8')
c4_lower = np.array([30, 45, 45], dtype='uint8')
"""

#data recording

angle_data_dict = {}
start_time = time.time()
record_rate_seconds = 1
last_recorded_time =  start_time

def add_entry(angle):
    global last_recorded_time
    time_cur = time.time()
    if time_cur >= last_recorded_time + record_rate_seconds:
        angle_data_dict[int(time_cur - start_time)] = angle
        last_recorded_time = time_cur
    
def save_angle_data(file_name):
    print(os.getcwd())

    # if not os.path.isdir(os.getcwd()+'AngleData'):
    #     os.makedirs(os.path.join(os.getcwd(),'AngleData'))
    #split the file name into a root and an extension
    root, ext = os.path.splitext(file_name)
    #adds any extra suffixes specified in the extra parameter. This is used to save the original and grey images and have them have a 
    #suffix at the end of their original name(eg. IMAGENAME_greyimage.jpeg)
    ext = ".csv"
    #root += datetime.today.strftime('%Y-%m-%d %H:%M:%S')
    file_path = root+ext
    with open(file_path,'x') as file:
       writer = csv.writer(file)
       writer.writerow(['Elapsed Time(seconds)', 'Angle Measured(degrees)'])
       for key, value in angle_data_dict.items():
            writer.writerow([key, value])

cv2.namedWindow("Webcam")
cv2.namedWindow("Filter")
cv2.setMouseCallback("Webcam", mouseClick, param=None)
kernel = np.ones((5,5), np.uint8)
while True:
    ret, frame = cap.read()

    #convert image to hsv
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #create 1st mask
    c1_mask = cv2.inRange(frame_hsv,c1_lower, c1_upper)
    c1_mask = cv2.erode(c1_mask, kernel, iterations=1)
    c1_filter = cv2.bitwise_or(frame, frame, mask = c1_mask)

    #create 2nd mask
    c2_mask = cv2.inRange(frame_hsv, c2_lower, c2_upper)
    c2_mask = cv2.erode(c2_mask, kernel, iterations=1)
    c2_filter = cv2.bitwise_or(frame, frame, mask=c2_mask)

    #create 3rd filter
    c3_mask = cv2.inRange(frame_hsv, c3_lower, c3_upper)
    c3_mask = cv2.erode(c3_mask, kernel, iterations=1)
    c3_filter = cv2.bitwise_or(frame, frame, mask=c3_mask)


    #create filtered image
    filtered_image = cv2.bitwise_or(c1_filter, c2_filter)
    filtered_image = cv2.bitwise_or(filtered_image, c3_filter)
    #centroid calculation
    c1_centroid = centroid_finder(c1_mask, filtered_image)
    c2_centroid = centroid_finder(c2_mask, filtered_image)
    c3_centroid = centroid_finder(c3_mask, filtered_image)
    
    #line drawing
    cv2.line(frame, c1_centroid, c2_centroid, [255,0,0], 3)
    cv2.line(frame, c2_centroid, c3_centroid, [255,0,0], 3)
    #cv2.line(frame, c3_centroid, c4_centroid, [255,0,0], 3)
    angle_cur = math_helpers.angle_finder(c1_centroid, c2_centroid, c3_centroid)
    filtered_image = cv2.putText(filtered_image, str(angle_cur), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255, 0, 0), 2, cv2.LINE_AA)

    add_entry(angle_cur)

    #debug
    #cv2.circle(frame, (int(c2_centroid[0]), int(c4_centroid[1])), 5, [0,0,255], -1)
    
    #print(math_helpers.angle_finder(c1_centroid, c2_centroid, c3_centroid))
    
    cv2.imshow("Webcam", frame)
    cv2.imshow("Filter", filtered_image)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(angle_data_dict)
file_name = input("What do you want to name the angle data file?(No extension needed)")
save_angle_data(file_name)