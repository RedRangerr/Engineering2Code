from re import I
import cv2
import logic

class ColorManager:
    def __init__(self, window_name, original_image, grayscale_image, original_colors = {}) -> None:
        self.current_color = 1
        self.colors = original_colors
        self.window_name = window_name
        self.original_image = original_image
        self.grayscale_image = grayscale_image
        cv2.createTrackbar("ColorB", window_name, 0, 255, lambda x:self.update_color_trackbars(0, x))
        cv2.createTrackbar("ColorG", window_name, 0, 255, lambda x:self.update_color_trackbars(1, x))
        cv2.createTrackbar("ColorR", window_name, 0, 255, lambda x:self.update_color_trackbars(2, x))
        cv2.createTrackbar("ColorBreak", window_name, 0, 255, lambda x:self.on_trackbar_update())
        cv2.createTrackbar("CurrentColor", window_name, 1, 6, lambda x:self.on_curent_color_trackbar_update(x))
        self.set_current_color(1)
        self.on_trackbar_update()

    def set_current_color(self, color_new):
        if (color_new < 1):
            return
        self.current_color = color_new
        cv2.setTrackbarPos("ColorB", self.window_name, self.colors[color_new][0])
        cv2.setTrackbarPos("ColorG", self.window_name, self.colors[color_new][1])
        cv2.setTrackbarPos("ColorR", self.window_name, self.colors[color_new][2])
    
    def on_trackbar_update(self):
        logic.refresh_image(self.grayscale_image, cv2.getTrackbarPos("ColorBreak", self.window_name), self.colors)
        
    def on_curent_color_trackbar_update(self,x):
        self.set_current_color(x)
    
    def update_color_trackbars(self, id, val):
        self.colors[self.current_color][id] = val
        logic.refresh_image(self.grayscale_image, cv2.getTrackbarPos("ColorBreak", self.window_name), self.colors)

    def get_customized_image(self):
        return logic.refresh_image(self.grayscale_image, cv2.getTrackbarPos("ColorBreak", self.window_name), self.colors, True)
        
    def get_greyscale_image(self):
        return self.grayscale_image
    
    def get_original_image(self):
        return self.original_image
    
    def get_graybreak_value(self):
        return cv2.getTrackbarPos("ColorBreak", self.window_name)
    
    def get_color_value(self, id):
        return self.colors[id]
