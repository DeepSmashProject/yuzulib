import time
from typing import List
import numpy as np
import requests
from .enums import Button
import matplotlib.pyplot as plt

class Client:
    def __init__(self, address="http://localhost:6000", disable_warning=False) -> None:
        self.address = address
        self.disable_warning = disable_warning

    def wait_server(self):
        pass

    def run_screen(self, callback, fps=15, render=False):
        print("run screen")
        url = '{}/screen'.format(self.address)
        if self.disable_warning:
            url = '{}/screen?disable_warning=true'.format(self.address)
        res = requests.post(url)
        time.sleep(1)
        self._stream_screen(callback, fps=fps, render=render)

    def _stream_screen(self, callback, fps=15, render=False):
        fig,ax = plt.subplots(1,1)
        first_plot = True
        im = None

        start = time.time()
        url = '{}/screen'.format(self.address)
        while True:
            res = requests.get(url)
            elapsed_time = time.time() - start
            target_elapsed_time = 1/fps
            if target_elapsed_time < elapsed_time:
                if not self.disable_warning:
                    print("warning: low fps {}".format(1/elapsed_time))
            else:
                time.sleep(target_elapsed_time-elapsed_time)
                elapsed_time = time.time() - start
            if res.status_code == 400:
                print("Error")
                break
            start = time.time()
            frame = res.json()["frame"]
            frame = np.array(frame)[:, :, :3].astype(np.uint8)
            # rendering
            if render:
                if first_plot:
                    im = ax.imshow(frame)
                    first_plot = False
                else:
                    im.set_data(frame)
                    fig.canvas.draw_idle()
                    plt.pause(0.001)

            callback(frame, 1/elapsed_time)

    def press(self, buttons: List[Button]):
        url = '{}/controller/press'.format(self.address)
        payload = {}
        params = {}
        res = requests.post(url)