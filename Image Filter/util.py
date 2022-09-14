import cv2
import numpy as np

#returns a depth mask for a specific color given a minimum and maximum gray value base on a min and max value
#in:min_gray: float
#in:max_gray: float
#out: [numpy.ndarry, numpy.ndarry]
def create_grayscale_arr(min_gray, max_gray):
    min_grayscale = [min_gray, min_gray, min_gray]
    max_grayscale = [max_gray, max_gray, max_gray]
    return [np.array(min_grayscale, dtype = "uint8"), np.array(max_grayscale, dtype = "uint8")]

def create_image_part(grayscale_image, min_grayscale, max_grayscale, color):
    block_all_but_certain_color = cv2.inRange(grayscale_image,min_grayscale,max_grayscale)
    image_height = grayscale_image.shape[0]
    image_width = grayscale_image.shape[1]
    image_channels = grayscale_image.shape[2]
    paper = np.zeros((image_height,image_width,image_channels), np.uint8)
    paper[0:image_height,0:image_width, 0:image_channels] = color
    return cv2.bitwise_or(paper, paper, mask= block_all_but_certain_color)    

    
    