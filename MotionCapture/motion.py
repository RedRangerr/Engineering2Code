# Physical Therapy Motion Capture Device Script
# Eng 4
# Bowie HS

# import libraries
import cv2
import numpy
import math
import time
import os
import csv
from pysine import sine



#Function for mouse clicks
def mouseClick(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv = frame_hsv[y,x]
        print("The mouse was clicked at x= ", x, "y = ", y)
        print("Hue = ", hsv[0],  "Sat = ", hsv[1], "Val = ", hsv[2])
       
def centroidFinder(input_image, output_image):
    moments = cv2.moments(input_image)
   
    if moments["m00"] == 0:
        centroid_x = 1
        centroid_y = 1
    else:
        centroid_x = moments["m10"]/moments["m00"]
        centroid_y = moments["m01"]/moments["m00"]
       
       
    cv2.circle(output_image, (int(centroid_x), int(centroid_y)), 5, (255, 255, 255), -1)
   
    return int(centroid_x), int(centroid_y)

def green(x):
    return(cv2.getTrackbarPos('Green', 'Filtered')+x)
def pink(x):
    return(cv2.getTrackbarPos('Pink', 'Filtered')+x)
def blue(x):
    return(cv2.getTrackbarPos('Blue', 'Filtered')+x)


angle_data_dict = {0:0}
start_time = time.time()

def add_entry(angle):
    global last_recorded_time
    time_cur = time.time()
    angle_data_dict[int(time_cur - start_time)] = angle

#saves a dictionary to a csv file
def save_angle_data(file_name, dict):
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
       for key, value in dict.items():
            writer.writerow([key, value])

#Function finds slope of lines
def angle_finder(a, b, c):
    #calc intersection point
    ab_vec = (a[0]-b[0], a[1]-b[1])
    bc_vec = (c[0]-b[0], c[1]-b[1])
    dot_product = ab_vec[0] * bc_vec[0] + ab_vec[1] * bc_vec[1]
    try:
        costheta = dot_product/(distance(a,b)* distance(b,c))
        return math.degrees(math.acos(costheta))
    except:
        return 0

def distance(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt(x*x + y*y)

print("'0' = internal camera. '1' = external camera. ")
camera = int(input("Which camera would you like to use?: "))
target = int(input("Enter your target angle: "))

target_angle = [int(target)+5, int(target)-5]

# initialize webcam
cap = cv2.VideoCapture(camera) #argument is webcam num

# Windows...
cv2.namedWindow("Webcam")
cv2.namedWindow("Filtered")
cv2.setMouseCallback("Webcam", mouseClick, param = None)
image = cv2.imread("Webcam")
cv2.createTrackbar('Blue', 'Filtered', 20, 30, lambda x:None)
cv2.createTrackbar('Pink', 'Filtered', 20, 30, lambda x:None)
cv2.createTrackbar('Green', 'Filtered', 20, 30, lambda x:None)

cv2.setTrackbarPos('Blue', 'Filtered', 0)
cv2.setTrackbarPos('Pink', 'Filtered', 0)
cv2.setTrackbarPos('Green', 'Filtered', 0)




keypressed = 0
kernel = numpy.ones((3, 3), numpy.uint8)


current_target = target
REST_ANGLE = 180

def switch_target():
    global current_target
    global target
    print("Current target: "+str(current_target), "Target Angle: "+str(target))
    if current_target == target:
        current_target = REST_ANGLE
    else:
        current_target = target
    print("New target: "+str(current_target))
    sine(duration=0.1)

def number_in_range(r, number, target):
    bound1 = target - r
    bound2 = target + r
    if number >= bound1 and number <= bound2:
        return "In Range"
    elif number < bound1:
        return "Low"
    return "High"


while keypressed != 27:
   
    #creating colors
    c1_upper = [blue(99), 255, 255] #HIGH DIVE
    c1_lower = [blue(94)-10, 110, 50]
    c1_upper = numpy.array(c1_upper, dtype = "uint8")
    c1_lower = numpy.array(c1_lower, dtype = "uint8")

    c3_upper = [pink(173), 140, 255] #LITTLE PRINCESS
    c3_lower = [pink(163)-10, 45, 100]
    c3_upper = numpy.array(c3_upper, dtype = "uint8")
    c3_lower = numpy.array(c3_lower, dtype = "uint8")

    c2_upper = [green(83), 120, 220]  #GARDEN STROLL
    c2_lower = [green(73)-10, 60, 70]
    c2_upper = numpy.array(c2_upper, dtype = "uint8")
    c2_lower = numpy.array(c2_lower, dtype = "uint8")


    # Captures image from camera
    ret, frame = cap.read()
   
    #create HSV image
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    c1_mask = cv2.inRange(frame_hsv, c1_lower, c1_upper)
    c1_mask = cv2.erode(c1_mask, kernel, iterations = 1)
    c2_mask = cv2.inRange(frame_hsv, c2_lower, c2_upper)
    c2_mask = cv2.erode(c2_mask, kernel, iterations = 1)
    c3_mask = cv2.inRange(frame_hsv, c3_lower, c3_upper)
    c3_mask = cv2.erode(c3_mask, kernel, iterations = 1)
   
   
    c1_filter = cv2.bitwise_or(frame, frame, mask = c1_mask)
    c2_filter = cv2.bitwise_or(frame, frame, mask = c2_mask)
    c3_filter = cv2.bitwise_or(frame, frame, mask = c3_mask)
   
   
    c1_cent = centroidFinder(c1_mask, frame)
    c2_cent = centroidFinder(c2_mask, frame)
    c3_cent = centroidFinder(c3_mask, frame)

    #calculate the current joint anglw
    angle = round(angle_finder(c1_cent, c2_cent, c3_cent))
   
    line_color = (0, 225, 255)
    # if angle > target_angle[0]:
    #     line_color = (0, 225, 255)
    # elif angle < target_angle[1]:
    #     line_color = (0, 0, 255)
    # else:
    #     line_color = (0, 255, 0)

    
    range_status = number_in_range(5, angle, current_target)
    #target angle
    if range_status == "In Range":
        line_color = (0, 255, 0)
        print("Hit target of "+str(current_target))
        add_entry(angle)
        switch_target()
    
    if angle <= target:
        line_color = (0, 0, 255)

       


    cv2.line(frame, (c1_cent[0], c1_cent[1]), (c2_cent[0], c2_cent[1]), line_color , 3) #line color, line thickness
    cv2.line(frame, (c2_cent[0], c2_cent[1]), (c3_cent[0], c3_cent[1]), line_color , 3) #line color, line thickness
   
   
   
    combined = cv2.bitwise_or(c1_filter, c2_filter)
    combined = cv2.bitwise_or(combined, c3_filter)
   
   
    coordinates = (c2_cent[0]+70, c2_cent[1]-70)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    printed_angle = cv2.putText(frame, str(angle), coordinates, font, fontScale, (255,255,255), 1, cv2.LINE_AA)
    target_angle = cv2.putText(frame, "Target angle:"+str(current_target), (50,50), font, fontScale, (0,0,255), 1, cv2.LINE_AA)
                               

 
   
    # Place image, refresh
    cv2.imshow("Webcam", frame)
    cv2.imshow("Filtered", combined)
    keypressed = cv2.waitKey(70)

# turn off webcam
cv2.destroyAllWindows()
cap.release()

#saves angle daTa
print(angle_data_dict)
file_name = input("What do you want to name the angle data file?(No extension needed)")   
while os.path.exists(file_name+".csv"):
    file_name += "`" 
save_angle_data(file_name, angle_data_dict)