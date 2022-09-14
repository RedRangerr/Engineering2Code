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

    

    
    