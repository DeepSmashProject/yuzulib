import time
import threading
import numpy as np
import cv2
from mss import mss

class Screen:
    def __init__(self, callback, fps=None):
        self.callback = callback
        self.fps = fps
        self.left, self.top, self.width, self.height = 0, 0, 100, 100

    #def set_window(self, left, top, width, height):
    #    self.left, self.top, self.width, self.height = left, top, width, height

    def run(self):
        thread = threading.Thread(target=self.capture)
        thread.start()

    def capture(self): 
        #left, top, width, height = 0, 0, 100, 100
        mon = {'left': self.left, 'top': self.top, 'width': self.width, 'height': self.height}
        start = time.time()

        with mss() as sct:
            while True:
                img = sct.grab(mon)
                frame = np.array(img)
                if cv2.waitKey(33) & 0xFF in (ord('q'), 27):
                    break
                
                self.callback()


def boil_udon():
    left, top, width, height = 0, 0, 100, 100
    mon = {'left': left, 'top': top, 'width': width, 'height': height}
    start = time.time()

    with mss() as sct:
        while True:
            img = sct.grab(mon)
            frame = np.array(img)
            if cv2.waitKey(33) & 0xFF in (ord('q'), 27):
                break
            print("frame")


print('うどんを作ります。')
def callback():
    print("callback")
screen = Screen(callback, fps=60)
screen.run()

print('盛り付けます。')
print('うどんができました。')

'''import asyncio
import time
async def func1():
    print('func1() started')
    await asyncio.sleep(1)
    print('func1() finished')

async def func2():
    print('func2() started')
    await asyncio.sleep(1)
    print('func2() finished')

async def main():
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())

loop = asyncio.get_event_loop()
loop.run_until_complete(func1())
print("aa")
time.sleep(3)
print("bb")'''