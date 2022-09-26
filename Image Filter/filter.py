# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os
import os.path
from logic import *

"""
Requirements
    [X]Output: Original Image, Grayscale image, and Customized Image.
    []Change colors
    []Make Instructions
    []Make Save option
    []Bonus: Save/Import Color combos   
    []Bonus: More than Six colors
    []Add comments
    
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
cv2.namedWindow("color_Trackbar")
cv2.namedWindow('Customized Image')
cv2.namedWindow("Original Image")
cv2.namedWindow("Grayscale Image")

#create sliders for grayscale breaks
cv2.createTrackbar("Color1Break", "Customized Image", 0, 255, lambda x:None)
# cv2.createTrackbar("Color2Break", "gray_Trackbar", 0, 255, lambda x:None)
# cv2.createTrackbar("Color3Break", "gray_Trackbar", 0, 255, lambda x:None)
# cv2.createTrackbar("Color4Break", "gray_Trackbar", 0, 255, lambda x:None)
# cv2.createTrackbar("Color5Break", "gray_Trackbar", 0, 255, lambda x:None)
# cv2.createTrackbar("Color6Break", "gray_Trackbar", 0, 255, lambda x:None)

#create sliders for color changes
cv2.createTrackbar("Color1B", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color1G", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color1R", "color_Trackbar", 0, 255, lambda x:None)

cv2.createTrackbar("Color2B", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color2G", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color2R", "color_Trackbar", 0, 255, lambda x:None)

cv2.createTrackbar("Color3B", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color3G", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color3R", "color_Trackbar", 0, 255, lambda x:None)

cv2.createTrackbar("Color4B", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color4G", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color4R", "color_Trackbar", 0, 255, lambda x:None)

cv2.createTrackbar("Color5B", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color5G", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color5R", "color_Trackbar", 0, 255, lambda x:None)

cv2.createTrackbar("Color6B", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color6G", "color_Trackbar", 0, 255, lambda x:None)
cv2.createTrackbar("Color6R", "color_Trackbar", 0, 255, lambda x:None)




keypressed = cv2.waitKey(30)

while keypressed != 27 and keypressed != ord('s'):
    #creates images of red and yellow images and a combined image which has red and yellow
    break_1 = cv2.getTrackbarPos("Color1Break", "Customized Image")
    break_2 = (break_1/6) * 2
    break_3 = (break_1/6) * 3
    break_4 = (break_1/6) * 4
    break_5 = (break_1/6) * 5
    break_6 = (break_1/6) * 6

    red_parts_of_image = create_image_part(grayscale_image, 0, break_1, [0,0,255])
    yellow_parts_of_image = create_image_part(grayscale_image, break_1+1, break_2, [0,255,255])
    green_parts_of_image = create_image_part(grayscale_image, break_2+1, break_3, [0,255,0])
    blue_parts_of_image = create_image_part(grayscale_image, break_3+1, break_4, [255, 0, 0])
    purple_parts_of_image = create_image_part(grayscale_image, break_4+1, break_5, [250, 230, 30])
    gold_parts_of_image = create_image_part(grayscale_image,  break_5+1, break_6, [38,162,193])

    customized_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, green_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, blue_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, purple_parts_of_image)
    customized_image = cv2.bitwise_or(customized_image, gold_parts_of_image)
    
    #shows windows
    cv2.imshow('Original Image',original_image)
    cv2.imshow('Grayscale Image',grayscale_image)
    cv2.imshow('Customized Image',customized_image)

    #check for keypress every 30ms
    keypressed = cv2.waitKey(30)
    if keypressed == 27:
        cv2.destroyAllWindows()
    elif keypressed == ord('s'): 
        file_name = input('Save Customized Image as:')
        save_image(file_name, customized_image)
        save_image(file_name, grayscale_image, '_grayscale')
        save_image(file_name, original_image, '_original')
        cv2.destroyAllWindows()

