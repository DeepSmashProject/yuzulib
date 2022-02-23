import numpy as np
import cv2
#from PIL import ImageGrab
import time
from mss import mss
from numpy.core.fromnumeric import take
from .util import Image, click_screen, is_exist_screen
from threading import (Event, Thread)
import pyautogui
import os
from pathlib import Path
import threading
import subprocess
class Screen:
    def __init__(self, callback, fps=None, disable_warning=False):
        self.disable_warning = disable_warning
        self.data_path = Path(os.path.dirname(__file__)).joinpath('data/').resolve()
        self.callback = callback
        self.fps = fps
        self.screen_size = self.get_screen_size()
        self.alive = True

    def click_init_yuzu(self):
        if is_exist_screen(Image.INIT_SCREEN):
            click_screen(Image.INIT_YES)

    def get_screen_size(self):
        self.click_init_yuzu()
        #self._take_screenshot()
        #(yuzu_left, yuzu_top, yuzu_width, yuzu_height) = self.get_locate_on_screen(Image.YUZU_SCREEN, confidence=.95)
        yuzu_left, yuzu_top, yuzu_width, yuzu_height = 214, 118, 853, 487
        (_, _, _, tb_height) = self.get_locate_on_screen(Image.TOP_BAR, confidence=.8)
        (_, _, _, bb_height) = self.get_locate_on_screen(Image.BOTTOM_BAR, confidence=.8)
        left, top, width, height = yuzu_left, yuzu_top+tb_height, yuzu_width, yuzu_height-tb_height-bb_height
        print("screen: ", left, top, width, height) # 214, 141, 853, 441
        return {"left": left, "top": top, "width": width, "height": height}

    def get_locate_on_screen(self, image, confidence=.9):
        count = 0
        while True:
            #if take_screen and count % 10 == 0:
            #    self._take_screenshot()
            result = pyautogui.locateOnScreen(image.value, confidence=confidence)
            if result != None:
                return result
            count += 1

    def run(self):
        thread = threading.Thread(target=self.capture)
        thread.start()

    def capture(self): 
        mon = {'left': self.screen_size["left"], 'top': self.screen_size["top"], 'width': self.screen_size["width"], 'height': self.screen_size["height"]}
        start = time.time()

        with mss() as sct:
            while self.alive:
                img = sct.grab(mon)
                frame = np.array(img)
                frame = np.array(frame)[:, :, :3] # bgra2bgr
                frame = frame[:,:,::-1]  # bgr2rgb
                if cv2.waitKey(33) & 0xFF in (ord('q'), 27):
                    break

                #cv2.imshow('test', frame)
                elapsed_time = time.time() - start
                if self.fps != None:
                    target_elapsed_time = 1/self.fps
                    if target_elapsed_time < elapsed_time:
                        if not self.disable_warning:
                            print("warning: low fps {}".format(1/elapsed_time))
                    else:
                        time.sleep(target_elapsed_time-elapsed_time)
                    elapsed_time = time.time() - start
                fps = 1/elapsed_time
                start = time.time()
                self.callback(frame, fps)

    def close(self):
        self.alive = False


if __name__ == '__main__':
    def callback(frame, fps):
        print("callback!", frame[0][0], fps)
    screen = Screen(callback, fps=60)
    screen.capture()
