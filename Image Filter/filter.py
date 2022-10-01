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

color_manager = ColorManager("Color_Controls", original_image, grayscale_image, colors_start)    

keypressed = cv2.waitKey(0)

while keypressed != 27 and keypressed != ord('s'):
    keypressed = cv2.waitKey(30)
    if keypressed == 27:
        cv2.destroyAllWindows()
    elif keypressed == ord('s'): 
        file_name = input('Save Customized Image as:')
        save_image(file_name, color_manager.get_customized_image())
        save_image(file_name, color_manager.get_greyscale_image(), '_grayscale')
        save_image(file_name, color_manager.get_original_image(), '_original')
        colorPath = input("Save color file as:")
        colors = {
            "gray_value": color_manager.get_graybreak_value(),
            "Color1": color_manager.get_color_value(1),
            "Color2": color_manager.get_color_value(2),
            "Color3": color_manager.get_color_value(3),
            "Color4": color_manager.get_color_value(4),
            "Color5": color_manager.get_color_value(5),
            "Color6": color_manager.get_color_value(6)
        }
        root, ext = os.path.splitext(colorPath)
        with open(root+".json", 'w') as f:
            json.dump(colors,f)
        cv2.destroyAllWindows()
