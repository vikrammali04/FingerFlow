import numpy as np
import cv2
from collections import deque

class ColorDrawer:
    """ The ColorDrawer class enables drawing on a virtual canvas with different colors (blue, green, red) and tracks drawn points using deques. It supports switching colors, clearing the canvas, and managing UI elements like color selection and clearing options. """
    def __init__(self):
        self.blue = [deque(maxlen=1024)]
        self.green = [deque(maxlen=1024)]
        self.red = [deque(maxlen=1024)]
        self.blue_index = 0
        self.green_index = 0
        self.red_index = 0
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        self.colorIndex = 0
        self.paintWindow = np.ones((471, 636, 3))

        self.setup_paint_window()

    def setup_paint_window(self):
        """
        Draws colored rectangles on the paint window at specific positions with specified colors and thickness.
        """
        cv2.putText(self.paintWindow, "CLEAR", (60, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(self.paintWindow, "BLUE", (180, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(self.paintWindow, "GREEN", (300, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(self.paintWindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2, cv2.LINE_AA)

    def clear_canvas(self):
        self.blue = [deque(maxlen=1024)]
        self.green = [deque(maxlen=1024)]
        self.red = [deque(maxlen=1024)]
        self.blue_index = 0
        self.green_index = 0
        self.red_index = 0
        self.paintWindow[67:, :, :] = 255

    def update_color_index(self, index):
        self.colorIndex = index

    def add_point(self, center):
        if self.colorIndex == 0:
            self.blue[self.blue_index].appendleft(center)
        elif self.colorIndex == 1:
            self.green[self.green_index].appendleft(center)
        elif self.colorIndex == 2:
            self.red[self.red_index].appendleft(center)

    def get_points(self):
        return [self.blue, self.green, self.red]
    
    def add_next_deques(self):
        """  Appends new empty deques for each color (blue, green, red) to separate the next set of drawn points. This ensures smooth continuation of the drawing without mixing coordinates from earlier strokes."""
        self.blue.append(deque(maxlen=512))
        self.blue_index += 1
        self.green.append(deque(maxlen=512))
        self.green_index += 1
        self.red.append(deque(maxlen=512))
        self.red_index += 1

    @staticmethod
    def update_camera_ui(frame):
        frame = cv2.rectangle(frame, (40, 1), (140, 65), (0, 0, 0), 2)
        frame = cv2.rectangle(frame, (160, 1), (260, 65), (255, 0, 0), 2)
        frame = cv2.rectangle(frame, (280, 1), (380, 65), (0, 255, 0), 2)
        frame = cv2.rectangle(frame, (400, 1), (500, 65), (0, 0, 255), 2)
        cv2.putText(frame, "CLEAR", (60, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "BLUE", (180, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "GREEN", (300, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2, cv2.LINE_AA)
        return frame


    

