# Images_01_Starting_Code
# Engineer Your World

import cv2
import numpy
import os.path
from util import *
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

#defines the image height, image width, and image channels
image_height = original_image.shape[0]
image_width = original_image.shape[1]
image_channels = original_image.shape[2]

#creates numpy arrays of the colors red and yellow
red_paper = numpy.zeros((image_height,image_width,image_channels), numpy.uint8)
yellow_paper = numpy.zeros((image_height,image_width,image_channels),
                           numpy.uint8)
red_paper[0:image_height,0:image_width, 0:image_channels] = [0,0,255]
yellow_paper[0:image_height,0:image_width, 0:image_channels] = [0,255,255]
#creates a threshold for depth masks to remove saturation
#grayscale_break = 100

# min_grayscale_for_red = [0,0,0]
# max_grayscale_for_red = [grayscale_break,grayscale_break,grayscale_break]
# min_grayscale_for_yellow = [grayscale_break+1,grayscale_break+1, 
#                             grayscale_break+1]
# max_grayscale_for_yellow = [255,255,255]

# min_grayscale_for_red = numpy.array(min_grayscale_for_red, dtype = "uint8")
# max_grayscale_for_red = numpy.array(max_grayscale_for_red, dtype = "uint8")
# min_grayscale_for_yellow = numpy.array(min_grayscale_for_yellow,
#                                        dtype = "uint8")
# max_grayscale_for_yellow = numpy.array(max_grayscale_for_yellow,
#                                        dtype = "uint8")
min_grayscale_for_red, max_grayscale_for_red = create_grayscale_arr(0,100)
min_grayscale_for_yellow, max_grayscale_for_yellow = create_grayscale_arr(100, 255)


block_all_but_the_red_parts = cv2.inRange(grayscale_image,
                                          min_grayscale_for_red,
                                          max_grayscale_for_red)
print(block_all_but_the_red_parts)
block_all_but_the_yellow_parts = cv2.inRange(grayscale_image,
                                             min_grayscale_for_yellow,
                                             max_grayscale_for_yellow)
print(block_all_but_the_yellow_parts)
#creates images of red and yellow images and a combined image which has red and yellow
# red_parts_of_image = cv2.bitwise_or(red_paper, red_paper,
#                                     mask = block_all_but_the_red_parts)
# yellow_parts_of_image = cv2.bitwise_or(yellow_paper, yellow_paper,
#                                        mask = block_all_but_the_yellow_parts)

red_parts_of_image = create_image_part(grayscale_image, 0, 100, [0,0,255])
yellow_parts_of_image = create_image_part(grayscale_image, 101, 255, [0,255,255])

customized_image = cv2.bitwise_or(red_parts_of_image, yellow_parts_of_image)

cv2.imshow('Original Image', original_image)
cv2.imshow('Grayscale Image',grayscale_image)
cv2.imshow('Red Parts of Image',red_parts_of_image)
cv2.imshow('Yellow Parts of Image',yellow_parts_of_image)
cv2.imshow('Customized Image',customized_image)

keypressed = cv2.waitKey(0)
if keypressed == 27:
    cv2.destroyAllWindows()
elif keypressed == ord('s'): 
    cv2.imwrite('photo_GS_1.jpg',grayscale_image)
    cv2.imwrite('photo_RY_1.jpg',customized_image)
    cv2.destroyAllWindows()