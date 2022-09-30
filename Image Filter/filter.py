# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os
import os.path
import json
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

cv2.namedWindow("Color1Part")
cv2.namedWindow("Color2Part")
cv2.namedWindow("Color3Part")
cv2.namedWindow("Color4Part")
cv2.namedWindow("Color5Part")
cv2.namedWindow("Color6Part")


#create slider for grayscale break
cv2.createTrackbar("Color1Break", "Customized Image", 0, 255, lambda x:refresh_image(grayscale_image))

#create sliders for color changes
cv2.createTrackbar("Color1B", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color1G", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color1R", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))

cv2.createTrackbar("Color2B", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color2G", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color2R", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))

cv2.createTrackbar("Color3B", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color3G", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color3R", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))

cv2.createTrackbar("Color4B", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color4G", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color4R", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))

cv2.createTrackbar("Color5B", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color5G", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color5R", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))

cv2.createTrackbar("Color6B", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color6G", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color6R", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))

cv2.createTrackbar("Color7B", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color7G", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))
cv2.createTrackbar("Color7R", "color_Trackbar", 0, 255, lambda x:refresh_image(grayscale_image))

#resizes thw window that has all the colors
cv2.resizeWindow("color_Trackbar", 300, 500)

colors = {}

def update_color(newVal, trackbar):
    global colors
    colors[trackbar] = newVal
    
refresh_image(grayscale_image)
keypressed = cv2.waitKey(0)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    file_name = input('Save Customized Image as:')
    save_image(file_name, refresh_image(grayscale_image, True))
    save_image(file_name, grayscale_image, '_grayscale')
    save_image(file_name, original_image, '_original')
    colors = {
        "gray_value": cv2.getTrackbarPos("Color1Break", "Customized Image"),
        "Color1": get_color(1),
        "Color2": get_color(2),
        "Color3": get_color(3),
        "Color4": get_color(4),
        "Color5": get_color(5),
        "Color6": get_color(6)
        }
    with open('colors.json', 'x') as f:
        json.dump(colors,f)
    cv2.destroyAllWindows()
