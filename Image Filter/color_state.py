import cv2
import logic

class ColorManager:
    def __init__(self, window_name, origin_image, original_colors = {}) -> None:
        self.current_color = 1
        self.colors = original_colors #{[b,g,r]}
        self.window_name = window_name
        self.origin_image = origin_image
        cv2.createTrackbar("ColorB", window_name, 0, 255, lambda x:self.on_trackbar_update())
        cv2.createTrackbar("ColorG", window_name, 0, 255, lambda x:self.on_trackbar_update())
        cv2.createTrackbar("ColorR", window_name, 0, 255, lambda x:self.on_trackbar_update())
        cv2.createTrackbar("ColorBreak", window_name, 0, 255, lambda x:self.on_trackbar_update())
        cv2.createTrackbar("CurrentColor", window_name, 1, 6, lambda x:self.on_curent_color_trackbar_update(x))
    
    def set_current_color(self, color_new):
        self.current_color = color_new
        cv2.setTrackbarPos("ColorB", self.window_name, self.colors[color_new][0])
        cv2.setTrackbarPos("ColorG", self.window_name, self.colors[color_new][1])
        cv2.setTrackbarPos("ColorR", self.window_name, self.colors[color_new][2])
    
    def on_trackbar_update(self):
        logic.refresh_image(self.origin_image, cv2.getTrackbarPos("ColorBreak", "Customized Image"), self.colors)
        
    def on_curent_color_trackbar_update(self,x):
        self.set_current_color(x)

        

