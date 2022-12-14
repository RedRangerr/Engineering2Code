# Physical Therapy Motion Capture Device Script
# Eng 4
# Bowie HS
#Elliot, Siddhu, Jake

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

#variable that stores what key is pressed
keypressed = 0
#variable that stores data about eroding the image
kernel = numpy.ones((3, 3), numpy.uint8)

#variable that stores the current angle the user needs to reach. The user must move their thumb back and forth between a rest angle and a target angle.
#The user will start at an angle of 180 degrees, then move it to the target angle inputted by the user, then the user will have to move back to an angle of 180 degrees 
current_target = target
#angle that the user has to go to after it hits the target angle
REST_ANGLE = 180

#switches the user's current target angle to the opposite.
def switch_target():
    #get access to the variables defined above
    global current_target
    global target
    print("Current target: "+str(current_target), "Target Angle: "+str(target))
    #if the current target is the angle given by the user, switch to the rest angle
    #otherwise, switch the target angle to the angle given by the user
    if current_target == target:
        current_target = REST_ANGLE
    else:
        current_target = target
    print("New target: "+str(current_target))
    #play a sound indicating the user has hit the current target and needs to switch
    sine(duration=0.1)

#checks if a number is in range of a target
#margin_of_error -> margin of error acceptable between the target and the given number
#number -> the number that we are testing to see if it is in range of a target
#target -> the target that we are checking to see if our given input falls in range of
def number_in_range(margin_of_error, number, target):
    #create bounds based on our target and margin of error
    bound1 = target - margin_of_error
    bound2 = target + margin_of_error
    #checks if the number is in range of the bounds
    #if it is, it returns "In Range", 
    # if it is lower than bound1 it returns "Low", 
    # if it is higher than bound2 it returns "High"
    if number >= bound1 and number <= bound2:
        return "In Range"
    elif number < bound1:
        return "Low"
    return "High"

#while we dont press the exit key
while keypressed != 27:
   
    #create hsv color bounds for the color HIGH DIVE(blue)
    c1_upper = [blue(99), 255, 255] #
    c1_lower = [blue(94)-10, 110, 50]
    #converts the upper and lower bounds of the HIGH DIVE color to numpy arrays
    c1_upper = numpy.array(c1_upper, dtype = "uint8")
    c1_lower = numpy.array(c1_lower, dtype = "uint8")

    #create hsv color bounds for the color GARDEN STROLL(green)
    c2_upper = [green(83), 120, 220]  #GARDEN STROLL
    c2_lower = [green(73)-10, 60, 70]
    #create hsv color bounds for the color GARDEN STROLL(green)
    c2_upper = numpy.array(c2_upper, dtype = "uint8")
    c2_lower = numpy.array(c2_lower, dtype = "uint8")


    #create hsv color bounds for the color LITTLE PRINCESS(pink)
    c3_upper = [pink(173), 140, 255] #LITTLE PRINCESS
    c3_lower = [pink(163)-10, 45, 100]
    #converts the upper and lower bounds of the LITTLE PRINCESS color to numpy arrays
    c3_upper = numpy.array(c3_upper, dtype = "uint8")
    c3_lower = numpy.array(c3_lower, dtype = "uint8")

    
    # Captures image from webcam
    ret, frame = cap.read()
   
    #converts the frame to HSV from BGR
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    #create a color mask that filters out all colors except those in range of the HIGH DIVE(blue) color and erodes it with the kernel variable defined previously
    c1_mask = cv2.inRange(frame_hsv, c1_lower, c1_upper)
    c1_mask = cv2.erode(c1_mask, kernel, iterations = 1)
    #create a color mask that filters out all colors except those in range of the GARDEN STROLL(green) color and erodes it with the kernel variable defined previously
    c2_mask = cv2.inRange(frame_hsv, c2_lower, c2_upper)
    c2_mask = cv2.erode(c2_mask, kernel, iterations = 1)
    #create a color mask that filters out all colors except those in range of the LITTLE PRINCESS(pink) color and erodes it with the kernel variable defined previously
    c3_mask = cv2.inRange(frame_hsv, c3_lower, c3_upper)
    c3_mask = cv2.erode(c3_mask, kernel, iterations = 1)
   
    #create a image that only contains the blue color in the original frame
    #by combing the original frame with itself then applying the blue mask created above
    c1_filter = cv2.bitwise_or(frame, frame, mask = c1_mask)
    #create a image that only contains the green color in the original frame
    #by combing the original frame with itself then applying the green mask created above
    c2_filter = cv2.bitwise_or(frame, frame, mask = c2_mask)
    #create a image that only contains the pink color in the original frame
    #by combing the original frame with itself then applying the pink mask created above
    c3_filter = cv2.bitwise_or(frame, frame, mask = c3_mask)
   
    #calculate the center cordinates of the blue color 
    c1_cent = centroidFinder(c1_mask, frame)
    #calculate the center cordinates of the green color 
    c2_cent = centroidFinder(c2_mask, frame)
    #calculate the center cordinates of the pink color 
    c3_cent = centroidFinder(c3_mask, frame)

    #calculate the current joint angle by passing in the centers of each color as a point then rounding it to get rid of decimals
    angle = round(angle_finder(c1_cent, c2_cent, c3_cent))
    
    #variable that stores the line color
    line_color = (0, 225, 255)


    #call the range function to see if the angle calculated above is in range of the programs CURRENT target anfle
    range_status = number_in_range(5, angle, current_target)
    #if the angle is in range
    if range_status == "In Range":
        #set the line color to green
        line_color = (0, 255, 0)
        #call the add entry function which records the calculated angle at the current time
        add_entry(angle)
        #switches the current target angle to be the oposite
        switch_target()
    
    #if our calculated angle is less than the angle that the user inputted at the beginning of the program
    #the user has moved too much which is dangerous
    if angle <= target:
        #set the angle color to red
        line_color = (0, 0, 255)

       

    #draw line from the blude centroid to the green centroid
    cv2.line(frame, (c1_cent[0], c1_cent[1]), (c2_cent[0], c2_cent[1]), line_color , 3) #line color, line thickness
    #draw line from the green centorid to the pink centroid
    cv2.line(frame, (c2_cent[0], c2_cent[1]), (c3_cent[0], c3_cent[1]), line_color , 3) #line color, line thickness
   
   
    #combine the image that contains only blue color with the image that has only green color 
    combined = cv2.bitwise_or(c1_filter, c2_filter)
    #combine the new image created above with blue and green with the image that only contains pink
    combined = cv2.bitwise_or(combined, c3_filter)
   
    #calculate cordinates where the text should be placed for our current angle
    coordinates = (c2_cent[0]+70, c2_cent[1]-70)
    #set font and fontscale
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    #place text that shows out current angle at the cordinates previosuly calculated
    printed_angle = cv2.putText(frame, str(angle), coordinates, font, fontScale, (255,255,255), 1, cv2.LINE_AA)
    #show the current target angle(the angle the user needs to currently reach) in the top left corner
    target_angle = cv2.putText(frame, "Target angle:"+str(current_target), (50,50), font, fontScale, (0,0,255), 1, cv2.LINE_AA)
                               

 
   
    #Show our main webcam in a cv2 window
    cv2.imshow("Webcam", frame)
    #show the image that only has our colors in a different cv2 window
    cv2.imshow("Filtered", combined)
    #wait 70 milliseconds for a keypress, the record whatever key was pressed. If it was the esc key, the while loop will terminate.
    keypressed = cv2.waitKey(70)

# turn off webcam
cv2.destroyAllWindows()
#dispose of the capture
cap.release()

#saves angle daTa
print(angle_data_dict)
#prompt the user to enter a name to save the angle data
file_name = input("What do you want to name the angle data file?(No extension needed)")   
#while the file path exists, add a tilda to the name so the program doens't crash 
# if we are trying to save a file with a name already taken by another file
while os.path.exists(file_name+".csv"):
    file_name += "`" 
#call the save angle function where we pass in the file_name given by the user and the angle_data dictionary, which we are going to save into a csv file
save_angle_data(file_name, angle_data_dict)