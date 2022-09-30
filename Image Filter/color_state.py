import cv2
import logic

class ColorManager:
    def __init__(self, window_name, origin_image, original_colors = {}) -> None:
        self.current_color = 1
        self.colors = original_colors #{[b,g,r]}
        self.window_name = window_name
        self.origin_image = origin_image
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
        print("Color id being updated.")
        self.current_color = color_new
        cv2.setTrackbarPos("ColorB", self.window_name, self.colors[color_new][0])
        cv2.setTrackbarPos("ColorG", self.window_name, self.colors[color_new][1])
        cv2.setTrackbarPos("ColorR", self.window_name, self.colors[color_new][2])
    
    def on_trackbar_update(self):
        print("refreshing image...")
        logic.refresh_image(self.origin_image, cv2.getTrackbarPos("ColorBreak", self.window_name), self.colors)
        
    def on_curent_color_trackbar_update(self,x):
        self.set_current_color(x)
    
    def update_color_trackbars(self, id, val):
        print(self.current_color)
        self.colors[self.current_color][id] = val
        logic.refresh_image(self.origin_image, cv2.getTrackbarPos("ColorBreak", self.window_name), self.colors)

    def get_image(self):
        return logic.refresh_image(self.origin_image, cv2.getTrackbarPos("ColorBreak", self.window_name), self.colors, True)
        
