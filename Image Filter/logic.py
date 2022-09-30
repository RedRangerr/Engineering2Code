import cv2
import numpy as np
import os
#returns a depth mask for a specific color given a minimum and maximum gray value base on a min and max value
#in:min_gray: float, minimum gray value
#in:max_gray: float, maximum gray value
#out: [numpy.ndarry, numpy.ndarry]
def create_grayscale_arr(min_gray, max_gray):
    min_grayscale = [min_gray, min_gray, min_gray]
    max_grayscale = [max_gray, max_gray, max_gray]
    return [np.array(min_grayscale, dtype = "uint8"), np.array(max_grayscale, dtype = "uint8")]

#returns a image that has only one color and black based on filtering grayscale values
#in:grayscale_image: 
def create_image_part(grayscale_image, min_grayscale, max_grayscale, color):
    min_grayscale_arr,max_grayscale_arr = create_grayscale_arr(min_grayscale, max_grayscale)
    block_all_but_certain_color = cv2.inRange(grayscale_image,min_grayscale_arr, max_grayscale_arr)
    image_height = grayscale_image.shape[0]
    image_width = grayscale_image.shape[1]
    image_channels = grayscale_image.shape[2]
    paper = np.zeros((image_height,image_width,image_channels), np.uint8)
    paper[0:image_height,0:image_width, 0:image_channels] = color
    return cv2.bitwise_or(paper, paper, mask= block_all_but_certain_color)    

#save an image safely
def save_image(file_name, image, extra = ''):
    if not os.path.isdir('Output'):
        os.makedirs('Output')
    root, ext = os.path.splitext(file_name)
    root += extra
    if not ext:
        ext = '.jpeg'
    cv2.imwrite('Output/'+root+ext, image)    

def get_color(id):
    whindow_name = "color_Trackbar"
    bar_base_name = "Color"+str(id)
    blue = bar_base_name+"B"
    green = bar_base_name+"G"
    red = bar_base_name+"R"
    return [cv2.getTrackbarPos(blue, whindow_name), cv2.getTrackbarPos(green, whindow_name), cv2.getTrackbarPos(red, whindow_name)]


def refresh_image(grey_image, return_image = False):
    break_1 = float(cv2.getTrackbarPos("Color1Break", "Customized Image"))/6
    break_2 = float(break_1) * 2
    break_3 = float(break_1) * 3
    break_4 = float(break_1) * 4
    break_5 = float(break_1) * 5
    break_6 = float(break_1) * 6

    color_1_parts = create_image_part(grey_image, 0, break_1, get_color(1))
    color_2_parts = create_image_part(grey_image, break_1+1, break_2, get_color(2))
    color_3_parts = create_image_part(grey_image, break_2+1, break_3, get_color(3))
    color_4_parts = create_image_part(grey_image, break_3+1, break_4, get_color(4))
    color_5_parts = create_image_part(grey_image, break_4+1, break_5, get_color(5))
    color_6_parts = create_image_part(grey_image,  break_5+1, break_6, get_color(6))

    customized_image = cv2.bitwise_or(color_1_parts, color_2_parts)
    customized_image = cv2.bitwise_or(customized_image, color_3_parts)
    customized_image = cv2.bitwise_or(customized_image, color_4_parts)
    customized_image = cv2.bitwise_or(customized_image, color_5_parts)
    customized_image = cv2.bitwise_or(customized_image, color_6_parts)
    
    #shows windows
    cv2.imshow('Color1Part', color_1_parts)
    cv2.imshow('Color2Part', color_2_parts)
    cv2.imshow('Color3Part', color_3_parts)
    cv2.imshow('Color4Part', color_4_parts)
    cv2.imshow('Color5Part', color_5_parts)
    cv2.imshow('Color6Part', color_6_parts)
    cv2.imshow('Customized Image',customized_image)
    if (return_image):
        return customized_image

def refresh_image(grey_image, grey_break, colors, return_image = False):
    break_1 = float(grey_break)/6
    break_2 = float(break_1) * 2
    break_3 = float(break_1) * 3
    break_4 = float(break_1) * 4
    break_5 = float(break_1) * 5
    break_6 = float(break_1) * 6

    color_1_parts = create_image_part(grey_image, 0, break_1, colors[0])
    color_2_parts = create_image_part(grey_image, break_1+1, break_2, colors[1])
    color_3_parts = create_image_part(grey_image, break_2+1, break_3, colors[2])
    color_4_parts = create_image_part(grey_image, break_3+1, break_4, colors[3])
    color_5_parts = create_image_part(grey_image, break_4+1, break_5, colors[4])
    color_6_parts = create_image_part(grey_image,  break_5+1, break_6, colors[5])

    customized_image = cv2.bitwise_or(color_1_parts, color_2_parts)
    customized_image = cv2.bitwise_or(customized_image, color_3_parts)
    customized_image = cv2.bitwise_or(customized_image, color_4_parts)
    customized_image = cv2.bitwise_or(customized_image, color_5_parts)
    customized_image = cv2.bitwise_or(customized_image, color_6_parts)
    
    #shows windows
    cv2.imshow('Color1Part', color_1_parts)
    cv2.imshow('Color2Part', color_2_parts)
    cv2.imshow('Color3Part', color_3_parts)
    cv2.imshow('Color4Part', color_4_parts)
    cv2.imshow('Color5Part', color_5_parts)
    cv2.imshow('Color6Part', color_6_parts)
    cv2.imshow('Customized Image',customized_image)
    if (return_image):
        return customized_image