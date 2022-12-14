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



#Function for keyboard events on a cv2 window
#event -> button that was pressed
#x -> x position of cordinate mouse pointer is currently at
#y -> y position of cordinate mouse pointer is currently at
def mouseClick(event, x, y, flags, params):
    #check if buton pressed is a left mouse button being pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        #get the pixel color in hsv from the x an y position of the mouse click and print it
        hsv = frame_hsv[y,x]
        print("The mouse was clicked at x= ", x, "y = ", y)
        print("Hue = ", hsv[0],  "Sat = ", hsv[1], "Val = ", hsv[2])

#finds the centroid of an image of a specific color and draws it on the screen
#input_image -> image that has a single color blob
#output image -> image that the center should be drawn to
def centroidFinder(input_image, output_image):
    #calculuate moments of image
    moments = cv2.moments(input_image)
   #calculate x and y cordinate of centroid based on the moments
    if moments["m00"] == 0:
        centroid_x = 1
        centroid_y = 1
    else:
        centroid_x = moments["m10"]/moments["m00"]
        centroid_y = moments["m01"]/moments["m00"]
       
    #draw the centroid on the output image
    cv2.circle(output_image, (int(centroid_x), int(centroid_y)), 5, (255, 255, 255), -1)
   
    #return the x and y cordinate as a tuple
    return int(centroid_x), int(centroid_y)

#get the current value of the green color for filtering
#x-> base green value
def green(x):
    #return the green trackbar value added to the base green value
    return(cv2.getTrackbarPos('Green', 'Filtered')+x)

#get the current value of the pink color for filtering
#x-> base pink value
def pink(x):
    #return the pink trackbar value added to the base green value
    return(cv2.getTrackbarPos('Pink', 'Filtered')+x)

#get the current value of the blue color for filtering
#x-> base blue value
def blue(x):
    #return the blue trackbar value added to the base green value
    return(cv2.getTrackbarPos('Blue', 'Filtered')+x)

#initalize dictionary that stores the current angle of the joint at specific timestamps
angle_data_dict = {}
#get the time when the program first runs. This is used to convert the current time relative to when the program started
start_time = time.time()

#adds an entry to the dictionary
#angle -> value of the angle to record
def add_entry(angle):
    #get current time
    time_cur = time.time()
    #get the amount of time that has passed since the program first ran
    elasped_time = int(time_cur - start_time)
    #record the data of the anfgle in the dictionary
    angle_data_dict[elasped_time] = angle

#saves a dictionary to a csv file
#file_name -> name of the file to save the dictionary as
#dict -> dictionary to save as a csv
def save_angle_data(file_name, dict):
    #split the file name into a root and an extension
    root, ext = os.path.splitext(file_name)
    #adds any extra suffixes specified in the extra parameter. This is used to save the original and grey images and have them have a 
    #suffix at the end of their original name(eg. IMAGENAME_greyimage.jpeg)
    ext = ".csv"
    #root += datetime.today.strftime('%Y-%m-%d %H:%M:%S')
    file_path = root+ext
    #open the file safely
    with open(file_path,'x') as file:
       #create a new instance of the csv writer
       writer = csv.writer(file)
       #write the headings to the file
       writer.writerow(['Elapsed Time(seconds)', 'Angle Measured(degrees)'])
       #write all the keys and values in the dictioanry to the csv file
       for key, value in dict.items():
            writer.writerow([key, value])

#Function finds the angle that 3 points make up
#a -> point a
#b -> point b
#c -> point c
def angle_finder(a, b, c):
    #Create two different vectors from the three points
    ab_vec = (a[0]-b[0], a[1]-b[1])
    bc_vec = (c[0]-b[0], c[1]-b[1])
    #calculate the dot product of the two vectors via the x and y components
    dot_product = ab_vec[0] * bc_vec[0] + ab_vec[1] * bc_vec[1]
    try:
        #solve for the angle using the alternate formula of the dot product(ABcos(theta))
        #calculate the cosine of the angle by dividing the dot_product by the 
        #product of the magnitudes of the two vectors which are aquired with the distance function below
        costheta = dot_product/(distance(a,b)* distance(b,c))
        return math.degrees(math.acos(costheta))
    except:
        #handles division by 0 error if the distance is 0
        return 0

#calculates the distance of two points via the distance formula(sqrt((x-x0)^2 + (y-y0)^2))
#p1 -> point 1
#p2 -> point 2
def distance(p1, p2):
    #get the x difference of the points
    x = p1[0] - p2[0]
    #get the y difference of the points
    y = p1[1] - p2[1]
    #use the distance formula to get the distance
    return math.sqrt(x*x + y*y)

#ask and store what camera the user wants to use
print("'0' = internal camera. '1' = external camera. ")
camera = int(input("Which camera would you like to use?: "))
#ask the user what their target angle is and store it
target = int(input("Enter your target angle: "))
#create a range of the target angle based on the user input
target_angle = [int(target)+5, int(target)-5]

# initialize webcam with camera user inputed
cap = cv2.VideoCapture(camera) #argument is webcam num

#Set up  Windows for the webcam and the color filter
cv2.namedWindow("Webcam")
cv2.namedWindow("Filtered")
#sets a mouse callback for the webcam when you click on it
cv2.setMouseCallback("Webcam", mouseClick, param = None)
#create trackbars for the different colors 
cv2.createTrackbar('Blue', 'Filtered', 20, 30, lambda x:None)
cv2.createTrackbar('Pink', 'Filtered', 20, 30, lambda x:None)
cv2.createTrackbar('Green', 'Filtered', 20, 30, lambda x:None)
#sets the trackbar psoitions to 0
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