import cv2
import numpy as np
import os
#returns a depth mask for a specific color given a minimum and maximum gray value base on a min and max value
#in:min_gray: float, minimum gray value
#in:max_gray: float, maximum gray value
#out: [numpy.ndarry, numpy.ndarry]
def create_grayscale_arr(min_gray, max_gray):
    #create a list with the same value for the min and max values
    min_grayscale = [min_gray, min_gray, min_gray]
    max_grayscale = [max_gray, max_gray, max_gray]
    #returns a list with the min and max values in a 3d format 
    return [np.array(min_grayscale, dtype = "uint8"), np.array(max_grayscale, dtype = "uint8")]

#returns a image that has only one color and black based on filtering grayscale values
def create_image_part(grayscale_image, min_grayscale, max_grayscale, color):
    #creates a color mask based on the min and max greyscale values
    min_grayscale_arr,max_grayscale_arr = create_grayscale_arr(min_grayscale, max_grayscale)
    block_all_but_certain_color = cv2.inRange(grayscale_image,min_grayscale_arr, max_grayscale_arr)
    #stores variables that represent the image width, image height, and the number of channels it has
    image_height = grayscale_image.shape[0]
    image_width = grayscale_image.shape[1]
    image_channels = grayscale_image.shape[2]
    #creates a paper the same size as the image as the original and assigns every pixel to the color parameter  so the image is completly one color
    paper = np.zeros((image_height,image_width,image_channels), np.uint8)
    paper[0:image_height,0:image_width, 0:image_channels] = color
    #return the image with some pixels set to black based on the mask created. This will be combines with other parts to complete the image.
    return cv2.bitwise_or(paper, paper, mask= block_all_but_certain_color)    

#save an image with a certain file name with the option to add an extra string to the name
def save_image(file_name, image, extra = ''):
    if not os.path.isdir('Output'):
        os.makedirs('Output')
    #split the file name into a root and an extension
    root, ext = os.path.splitext(file_name)
    #adds any extra suffixes specified in the extra parameter. THis is used to save the original and grey images and have them have a 
    #suffix at the end of their original name(eg. IMAGENAME_greyimage.jpeg)
    root += extra
    #adds a jpg file extension if there isnt one already
    if not ext:
        ext = '.jpeg'
    #saves the image based on the modified path and the image provided in the parameter.
    cv2.imwrite('Output/'+root+ext, image)    

#refreshes the image based on a greybreak value and color values with the option to return the image
def refresh_image(grey_image, grey_break, colors, return_image = False):
    #creates break values for each color dynamically based on one value. This allows us to have only one slider to control the greyscale breaks
    break_1 = float(grey_break)/10
    break_2 = float(break_1) * 2
    break_3 = float(break_1) * 3
    break_4 = float(break_1) * 4
    break_5 = float(break_1) * 5
    break_6 = float(break_1) * 6
    break_7 = float(break_1) * 7
    break_8 = float(break_1) * 8
    break_9 = float(break_1) * 9
    
    #calls the create_image_part function for each color given in the color dictionary and creates image parts for each one
    color_1_parts = create_image_part(grey_image, 0, break_1, colors[1])
    color_2_parts = create_image_part(grey_image, break_1+1, break_2, colors[2])
    color_3_parts = create_image_part(grey_image, break_2+1, break_3, colors[3])
    color_4_parts = create_image_part(grey_image, break_3+1, break_4, colors[4])
    color_5_parts = create_image_part(grey_image, break_4+1, break_5, colors[5])
    color_6_parts = create_image_part(grey_image,  break_5+1, break_6, colors[6])
    color_7_parts = create_image_part(grey_image,  break_6+1, break_7, colors[7])
    color_8_parts = create_image_part(grey_image,  break_7+1, break_8, colors[8])
    color_9_parts = create_image_part(grey_image,  break_8+1, break_9, colors[9])
    color_10_parts = create_image_part(grey_image,  break_9+1, 255, colors[10])

    #cobine all the image parts into one image
    customized_image = cv2.bitwise_or(color_1_parts, color_2_parts)
    customized_image = cv2.bitwise_or(customized_image, color_3_parts)
    customized_image = cv2.bitwise_or(customized_image, color_4_parts)
    customized_image = cv2.bitwise_or(customized_image, color_5_parts)
    customized_image = cv2.bitwise_or(customized_image, color_6_parts)
    customized_image = cv2.bitwise_or(customized_image, color_7_parts)
    customized_image = cv2.bitwise_or(customized_image, color_8_parts)
    customized_image = cv2.bitwise_or(customized_image, color_9_parts)
    customized_image = cv2.bitwise_or(customized_image, color_10_parts)
    #refresh the image on the cv2 window
    cv2.imshow('Customized Image',customized_image)
    if (return_image):
        #returns the image if we specify it to
        return customized_image