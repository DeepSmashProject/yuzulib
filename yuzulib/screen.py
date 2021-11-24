import numpy as np
import cv2
#from PIL import ImageGrab
import time
from mss import mss
from numpy.core.fromnumeric import take
from .util import Image
from threading import (Event, Thread)
import pyautogui
import os
from pathlib import Path
import threading
import subprocess
class Screen:
    def __init__(self, callback, fps=None):
        self.data_path = Path(os.path.dirname(__file__)).joinpath('data/').resolve()
        self.callback = callback
        self.fps = fps
        self.screen_size = self.get_screen_size()
        self.alive = True

    def _take_screenshot(self):
        filename = Image.YUZU_SCREEN.value
        # delete screenshot
        if os.path.isfile(filename):
            os.remove(filename)

        command = "scrot {} -u".format(filename)
        proc = subprocess.run(command, shell=True, executable='/bin/bash')
        if proc.returncode == 0:
            print("Take screenshot successfully")
        return filename

    def get_screen_size(self):
        #self._take_screenshot()
        (yuzu_left, yuzu_top, yuzu_width, yuzu_height) = self.get_locate_on_screen(Image.YUZU_SCREEN, take_screen=True)
        (_, _, _, tb_height) = self.get_locate_on_screen(Image.TOP_BAR)
        (_, _, _, bb_height) = self.get_locate_on_screen(Image.BOTTOM_BAR)
        left, top, width, height = yuzu_left, yuzu_top+tb_height, yuzu_width, yuzu_height-tb_height-bb_height
        print("screen: ", left, top, width, height)
        return {"left": left, "top": top, "width": width, "height": height}

    def get_locate_on_screen(self, image, take_screen=False):
        count = 0
        while True:
            count += 1
            if take_screen and count % 10 == 0:
                self._take_screenshot()
            result = pyautogui.locateOnScreen(image.value, confidence=.9)
            if result != None:
                return result

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

    def close(self):
        self.alive = False


if __name__ == '__main__':
    def callback(frame, fps):
        print("callback!", frame[0][0], fps)
    screen = Screen(callback, fps=60)
    screen.capture()
