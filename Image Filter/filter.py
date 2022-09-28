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
    [X]Change colors
    []Make Instructions
    [X]Make Save option
    []Bonus: Save/Import Color combos   
    []Bonus: More than Six colors
    [X]Add comments
    
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

#create slider for grayscale break
cv2.createTrackbar("Color1Break", "Customized Image", 0, 255, lambda x:refresh_image())

#create sliders for color changes
cv2.createTrackbar("Color1B", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color1G", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color1R", "color_Trackbar", 0, 255, lambda x:refresh_image())

cv2.createTrackbar("Color2B", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color2G", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color2R", "color_Trackbar", 0, 255, lambda x:refresh_image())

cv2.createTrackbar("Color3B", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color3G", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color3R", "color_Trackbar", 0, 255, lambda x:refresh_image())

cv2.createTrackbar("Color4B", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color4G", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color4R", "color_Trackbar", 0, 255, lambda x:refresh_image())

cv2.createTrackbar("Color5B", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color5G", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color5R", "color_Trackbar", 0, 255, lambda x:refresh_image())

cv2.createTrackbar("Color6B", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color6G", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color6R", "color_Trackbar", 0, 255, lambda x:refresh_image())

cv2.createTrackbar("Color7B", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color7G", "color_Trackbar", 0, 255, lambda x:refresh_image())
cv2.createTrackbar("Color7R", "color_Trackbar", 0, 255, lambda x:refresh_image())

#resizes thw window that has all the colors
cv2.resizeWindow("color_Trackbar", 300, 500)

#gets the value of a specifc color trackbar on the color_Trackbar window
def get_color(id):
    whindow_name = "color_Trackbar"
    bar_base_name = "Color"+str(id)
    blue = bar_base_name+"B"
    green = bar_base_name+"G"
    red = bar_base_name+"R"
    return [cv2.getTrackbarPos(blue, whindow_name), cv2.getTrackbarPos(green, whindow_name), cv2.getTrackbarPos(red, whindow_name)]   

#refreshes the customized image based on the slider value
def refresh_image(return_image = False):
    break_1 = cv2.getTrackbarPos("Color1Break", "Customized Image")
    break_2 = (break_1/6) * 2
    break_3 = (break_1/6) * 3
    break_4 = (break_1/6) * 4
    break_5 = (break_1/6) * 5
    break_6 = (break_1/6) * 6
    break_7 = (break_1/6) * 7
    
    color_1_parts = create_image_part(grayscale_image, 0, break_1, get_color(1))
    color_2_parts = create_image_part(grayscale_image, break_1+1, break_2, get_color(2))
    color_3_parts = create_image_part(grayscale_image, break_2+1, break_3, get_color(3))
    color_4_parts = create_image_part(grayscale_image, break_3+1, break_4, get_color(4))
    color_5_parts = create_image_part(grayscale_image, break_4+1, break_5, get_color(5))
    color_6_parts = create_image_part(grayscale_image,  break_5+1, break_6, get_color(6))
    color_7_parts = create_image_part(grayscale_image, break_6+1, break_6, get_color(7))

    customized_image = cv2.bitwise_or(color_1_parts, color_2_parts)
    customized_image = cv2.bitwise_or(customized_image, color_3_parts)
    customized_image = cv2.bitwise_or(customized_image, color_4_parts)
    customized_image = cv2.bitwise_or(customized_image, color_5_parts)
    customized_image = cv2.bitwise_or(customized_image, color_6_parts)
    customized_image = cv2.bitwise_or(customized_image, color_7_parts)

    #shows windows
    cv2.imshow('Original Image',original_image)
    cv2.imshow('Grayscale Image',grayscale_image)
    cv2.imshow('Customized Image',customized_image)
    if (return_image):
        return customized_image


refresh_image()
keypressed = cv2.waitKey(0)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    file_name = input('Save Customized Image as:')
    save_image(file_name, refresh_image(True))
    save_image(file_name, grayscale_image, '_grayscale')
    save_image(file_name, original_image, '_original')
    cv2.destroyAllWindows()