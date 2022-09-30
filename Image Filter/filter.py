# Images_01_Starting_Code
# Engineer Your World
import cv2
import numpy
import os
import os.path
import json
from logic import *
from color_state import ColorManager
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

json_option = input("Would you like to load colors? (Y/N) ")
if json_option == "Y":
    with open(input("Enter the file name:"), 'r') as input_file:
        pass
        
        
    


#creates windows
cv2.namedWindow("Color_Controls")
cv2.namedWindow('Customized Image')
# cv2.namedWindow("Original Image")
# cv2.namedWindow("Grayscale Image")

# cv2.namedWindow("Color1Part")
# cv2.namedWindow("Color2Part")
# cv2.namedWindow("Color3Part")
# cv2.namedWindow("Color4Part")
# cv2.namedWindow("Color5Part")
# cv2.namedWindow("Color6Part")

colors_start = {1:[0,0,0], 2:[0,0,0], 3:[0,0,0], 4:[0,0,0], 5:[0,0,0], 6:[0,0,0]}

color_manager = ColorManager("Color_Controls", grayscale_image, colors_start)

#resizes thw window that has all the colors
cv2.resizeWindow("Color_Controls", 300, 500)
    

keypressed = cv2.waitKey(0)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    file_name = input('Save Customized Image as:')
    save_image(file_name, color_manager.get_image())
    save_image(file_name, grayscale_image, '_grayscale')
    save_image(file_name, original_image, '_original')
    colorPath = input("Save color file as:")
    colors = {
        "gray_value": cv2.getTrackbarPos("Color1Break", "Customized Image"),
        "Color1": get_color(1),
        "Color2": get_color(2),
        "Color3": get_color(3),
        "Color4": get_color(4),
        "Color5": get_color(5),
        "Color6": get_color(6)
        }
    with open(colorPath, 'x') as f:
        json.dump(colors,f)
    cv2.destroyAllWindows()
