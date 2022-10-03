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
    [X]Bonus: Save/Import Color combos   
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

#asks the user if they want to load in json data to preset the colors
json_option = input("Would you like to load colors? (Y/N) ")
json_file = None
if json_option == "Y" or json_option == "y":
    while True:
        file_name = input("Enter the file name:")
        if not os.path.isfile(file_name):
            try_again_str = input("Couldn't find the file path specified. Do you want to try again?(y/n)")
            if not try_again_str == "y":
                break
            else:
                continue
        else:
            with open(file_name, 'r') as f:
                json_file = json.load(f)
                cv2.destroyAllWindows()
            print("Loaded color combinations!")
            break

#function to deserialize a json file into a dictionary of colors and a greyscale value
def try_deserialize_json(dict):
    gray_value = dict['gray_value']
    colors = {}
    for i in range(1, len(dict)):
        colors[i] = dict[str(i)]
    return (gray_value, colors) 

#creates windows
cv2.namedWindow("Color_Controls")
cv2.namedWindow('Customized Image')

#defines variables for the starting grayscale value and color dictionary
greybreak_start = 0
colors_start = {1:[0,0,0], 2:[0,0,0], 3:[0,0,0], 4:[0,0,0], 5:[0,0,0], 6:[0,0,0], 7:[0,0,0], 8:[0,0,0], 9:[0,0,0], 10:[0,0,0]}
#if there was a json file loaded in, it will deserialize it and set the previously defined variables to the values in the json file
if json_file != None:
    data = try_deserialize_json(json_file)
    greybreak_start = data[0]
    colors_start = data[1]
    print(colors_start)
    
#creates a new instance of the color manager class
color_manager = ColorManager("Color_Controls", original_image, grayscale_image, greybreak_start, colors_start)    


save_stuff = False

customized_image = None
original_image = None
grayscale_image = None
colors = None
keypressed = cv2.waitKey(30)
while keypressed != 27 and keypressed != ord('s'):
    keypressed = cv2.waitKey(30)
    if keypressed == 27:
        cv2.destroyAllWindows()
    elif keypressed == ord('s'): 
        save_stuff = True
        customized_image = color_manager.get_customized_image()
        original_image = color_manager.get_original_image()
        grayscale_image = color_manager.get_greyscale_image()
        colors = color_manager.get_state()
        cv2.destroyAllWindows()

if save_stuff:
    file_name = input('Save Customized Image as:')
    save_image(file_name, customized_image)
    save_image(file_name, grayscale_image, '_grayscale')
    save_image(file_name, original_image, '_original')
    colorPath = input("Save color file as:")
    root, ext = os.path.splitext(colorPath)
    with open(root+".json", 'w') as f:
        json.dump(colors,f)
        cv2.destroyAllWindows()