from re import I
import cv2
import logic

#class to manage the states of all the colors
class ColorManager:
    #initializes the class with a window name, original image, grey image, a value for the greybreak value, and a dictionary of colors that map ids to a list of rgb values
    def __init__(self, window_name, original_image, grayscale_image, greybreak_val = 0, original_colors = {}) -> None:
        #creates instance variables
        self.current_color = 1#the color that we are currently editing
        self.colors = original_colors#all of our colors
        self.window_name = window_name#our window name
        self.original_image = original_image#our original image
        self.grayscale_image = grayscale_image#our grayscale image
        #create trackbars for editing the bgr values of the color 
        #the lamda functions trigger updates to the image and color data of the class 
        cv2.createTrackbar("ColorB", window_name, 0, 255, lambda x:self.update_color_trackbars(0, x))
        cv2.createTrackbar("ColorG", window_name, 0, 255, lambda x:self.update_color_trackbars(1, x))
        cv2.createTrackbar("ColorR", window_name, 0, 255, lambda x:self.update_color_trackbars(2, x))
        #greyscale break trackbar which controls how the different colors are divided withn the image
        #the lamda updates the grey value
        cv2.createTrackbar("ColorBreak", window_name, 0, 255, lambda x:self.on_trackbar_update())
        cv2.createTrackbar("CurColor", window_name, 1, 10, lambda x:self.on_curent_color_trackbar_update(x))
        #set the greyscale trackbar equal to the value of 
        if greybreak_val != 0:
            cv2.setTrackbarPos("ColorBreak", window_name, greybreak_val)
        #function that updates the current color to the 1st bar
        self.set_current_color(1)
        #updates the image
        self.on_trackbar_update()

    #function that sets the current color and updates the trackbar based on its value
    def set_current_color(self, color_new):
        if (color_new < 1):
            return
        self.current_color = color_new
        cv2.setTrackbarPos("ColorB", self.window_name, self.colors[color_new][0])
        cv2.setTrackbarPos("ColorG", self.window_name, self.colors[color_new][1])
        cv2.setTrackbarPos("ColorR", self.window_name, self.colors[color_new][2])
    
    #refreshes the final image with the current color and grey break values
    def on_trackbar_update(self):
        logic.refresh_image(self.grayscale_image, cv2.getTrackbarPos("ColorBreak", self.window_name), self.colors)
    
    #sets the current color when
    def on_curent_color_trackbar_update(self,x):
        self.set_current_color(x)
    
    #function is called when any of the color sliders are updated
    #updates the current color's value with the new value and reloads the image
    def update_color_trackbars(self, id, val):
        self.colors[self.current_color][id] = val
        logic.refresh_image(self.grayscale_image, cv2.getTrackbarPos("ColorBreak", self.window_name), self.colors)

    #refreshes and returns the final image
    def get_customized_image(self):
        return logic.refresh_image(self.grayscale_image, cv2.getTrackbarPos("ColorBreak", self.window_name), self.colors, True)
    
    #returns the greyscale image
    def get_greyscale_image(self):
        return self.grayscale_image
    
    #returns the original image
    def get_original_image(self):
        return self.original_image
    
    #returns the current value of the greybreak
    def get_graybreak_value(self):
        return cv2.getTrackbarPos("ColorBreak", self.window_name)
    
    #returns the value of a specfic color(max val of 10 since there are only 10 different colors)
    def get_color_value(self, id):
        return self.colors[id]
    
    #returns a dictionary with the color ids mapping to color values and a string mapping to the current greybreak
    #this is used to serialize all the data into json
    def get_state(self):
        dict = {}
        dict['gray_value'] = cv2.getTrackbarPos("ColorBreak", self.window_name)
        for key in self.colors:
            dict[key] = self.colors[key]
        return dict