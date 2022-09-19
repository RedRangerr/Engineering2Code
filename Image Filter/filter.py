# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path
from logic import *
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

#creates winows
cv2.namedWindow('Original Image')
cv2.namedWindow('Grayscale Image')
cv2.namedWindow('Red Parts of Image')
cv2.namedWindow('Yellow Parts of Image')
cv2.namedWindow('Customized Image')


#creates images of red and yellow images and a combined image which has red and yellow
red_parts_of_image = create_image_part(grayscale_image, 0, 50, [0,0,255])
yellow_parts_of_image = create_image_part(grayscale_image, 51, 120, [0,255,255])
green_parts_of_image = create_image_part(grayscale_image, 121, 180, [0,255,0])
blue_parts_of_image = create_image_part(grayscale_image, 181, 220, [255, 0, 0])
#30,230,250
purple_parts_of_image = create_image_part(grayscale_image, 221, 255, [250, 230, 30])

customized_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)
customized_image = cv2.bitwise_or(customized_image, green_parts_of_image)
customized_image = cv2.bitwise_or(customized_image, blue_parts_of_image)
customized_image = cv2.bitwise_or(customized_image, purple_parts_of_image)




cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)
cv2.imshow('Red Parts of Image',red_parts_of_image)
cv2.imshow('Yellow Parts of Image',purple_parts_of_image)
cv2.imshow('Customized Image',customized_image)

keypressed = cv2.waitKey(0)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()