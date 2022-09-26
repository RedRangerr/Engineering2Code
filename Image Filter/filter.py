# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path
from logic import *

"""
Requirements
    Output: Original Image, Grayscale image, and Customized Image.
    Make Instructions
    Make Save option
Bonus: Save/Import Color combos
Bonus: More than Six colors
    Add comments
    Change colors
"""



#gets the image from the user



print ("Save your original image in the same folder as this program.")
filename_valid = False
while filename_valid == False:
    filename = input("Enter the name of your file, including the "\
                                 "extension, and then press 'enter': ")
    if os.path.isfile(filename) == True:
        filename_valid = True
    else:
        print ("Something was wrong with that filename. Please try again.")

#reads the image provided by the user
original_image = cv2.imread(filename,1)
grayscale_image_simple = cv2.imread(filename, 0)
grayscale_image = cv2.cvtColor(grayscale_image_simple, cv2.COLOR_GRAY2BGR)

#creates windows
cv2.namedWindow("Trackbar")
cv2.namedWindow('Customized Image')

#create sliders for colors
cv2.createTrackbar("Color1Break", "Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color2Break", "Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color3Break", "Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color4Break", "Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color5Break", "Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color6Break", "Trackbar", 0, 255, lambda x:None)



keypressed = cv2.waitKey(30)

while keypressed != 27 and keypressed != ord('s'):
    #creates images of red and yellow images and a combined image which has red and yellow
    red_parts_of_image = create_image_part(grayscale_image, 0, cv2.getTrackbarPos("Color1Break", "Trackbar"), [0,0,255])
    yellow_parts_of_image = create_image_part(grayscale_image, cv2.getTrackbarPos("Color1Break", "Trackbar")+1, cv2.getTrackbarPos("Color2Break", "Trackbar"), [0,255,255])
    green_parts_of_image = create_image_part(grayscale_image, cv2.getTrackbarPos("Color2Break", "Trackbar")+1, cv2.getTrackbarPos("Color3Break", "Trackbar"), [0,255,0])
    blue_parts_of_image = create_image_part(grayscale_image, cv2.getTrackbarPos("Color3Break", "Trackbar")+1, cv2.getTrackbarPos("Color4Break", "Trackbar"), [255, 0, 0])
    purple_parts_of_image = create_image_part(grayscale_image, cv2.getTrackbarPos("Color4Break", "Trackbar")+1, cv2.getTrackbarPos("Color5Break", "Trackbar"), [250, 230, 30])
    gold_parts_of_image = create_image_part(grayscale_image,  cv2.getTrackbarPos("Color5Break", "Trackbar")+1, cv2.getTrackbarPos("Color6Break", "Trackbar"), [38,162,193])

    customized_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, green_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, blue_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, purple_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, gold_parts_of_image)
    #shows windows
    cv2.imshow('Red Parts of Image',red_parts_of_image)
    cv2.imshow('Yellow Parts of Image',purple_parts_of_image)
    cv2.imshow('Customized Image',customized_image)

    #check for keypress every 30ms
    keypressed = cv2.waitKey(30)
    if keypressed == 27:
        cv2.destroyAllWindows()
    elif keypressed == ord('s'): 
        file_name = input('Save Customized Image as:')
        cv2.imwrite("OutputImages/"+file_name,customized_image)
        cv2.destroyAllWindows()

