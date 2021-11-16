import numpy as np
import cv2
#from PIL import ImageGrab
import time
from mss import mss
from PIL import Image
from threading import (Event, Thread)
import pyautogui
import os
from pathlib import Path
class Screen:
    def __init__(self, callback, fps=None):
        self.data_path = Path(os.path.dirname(__file__)).joinpath('data/').resolve()
        self.callback = callback
        self.fps = fps
        self.left, self.top, self.width, self.height = 0, 0, 0, 0

    #def set_window(self, left, top, width, height):
    #    self.left, self.top, self.width, self.height = left, top, width, height

    async def capture(self): 
        mon = {'left': self.left, 'top': self.top, 'width': self.width, 'height': self.height}
        start = time.time()

        with mss() as sct:
            while True:
                img = sct.grab(mon)
                frame = np.array(img)
                if cv2.waitKey(33) & 0xFF in (ord('q'), 27):
                    break

                #cv2.imshow('test', frame)
                elapsed_time = time.time() - start
                if self.fps != None:
                    target_elapsed_time = 1/self.fps
                    if target_elapsed_time < elapsed_time:
                        print("warning: low fps")
                    else:
                        time.sleep(target_elapsed_time-elapsed_time)
                    elapsed_time = time.time() - start
                fps = 1/elapsed_time
                start = time.time()
                self.callback(frame, fps)


if __name__ == '__main__':
    def callback(frame, fps):
        print("callback!", frame[0][0], fps)
    screen = Screen(callback, fps=60)
    screen.capture()
