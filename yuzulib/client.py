import time
from typing import List
import numpy as np
import requests
from .enums import Button
import matplotlib.pyplot as plt

def register_to_server(address="http://localhost:6000"):
    url = '{}/server/register'.format(address)
    try:
        res = requests.post(url, timeout=1)
        print(res)
        if res.status_code == 200:
            return True
        return False
    except Exception:
        return False

def unregister_to_server(address="http://localhost:6000"):
    url = '{}/server/unregister'.format(address)
    try:
        res = requests.post(url, timeout=1)
        print(res)
        if res.status_code == 200:
            return True
        return False
    except Exception:
        return False

class Client:
    def __init__(self, address="http://localhost:6000", disable_warning=False) -> None:
        self.address = address
        self.disable_warning = disable_warning

    def run_screen(self, callback, fps=15, render=False, width=256, height=256, grayscale=False):
        print("run screen")
        url = '{}/screen/'.format(self.address)
        if self.disable_warning:
            url = '{}/screen/?disable_warning=true'.format(self.address)
        res = requests.post(url)
        time.sleep(1)
        self._stream_screen(callback, fps=fps, render=render, width=width, height=height, grayscale=grayscale)

    def _stream_screen(self, callback, fps=15, render=False, width=256, height=256, grayscale=False):
        if render:
            fig,ax = plt.subplots(1,1)
            first_plot = True
            im = None

        start = time.time()
        payload = {"size": {"width": width, "height": height}, "grayscale": grayscale}
        url = '{}/screen/'.format(self.address)
        while True:
            res = requests.get(url, json=payload)
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
            data = res.json()
            frame = np.array(data["frame"]).astype(np.uint8)
            # rendering
            if render:
                if first_plot:
                    im = ax.imshow(frame)
                    first_plot = False
                else:
                    im.set_data(frame)
                    fig.canvas.draw_idle()
                    plt.pause(0.001)

            callback(frame, 1/elapsed_time, data["info"])

    def press(self, buttons: List[Button], hold=False, sec=0, wait=0):
        url = '{}/controller/press'.format(self.address)
        buttons = [bt.name for bt in buttons]
        payload = {"buttons": buttons}
        params = {"hold": hold, "sec": sec, "wait": wait}
        res = requests.post(url, json=payload, params=params)

    def run_game(self, game_path: str, dlc_dir: str):
        url = '{}/runner/run_game'.format(self.address)
        payload = {"game_path": game_path, "dlc_dir": dlc_dir}
        res = requests.post(url, json=payload)

    def reset_game(self):
        url = '{}/runner/reset_game'.format(self.address)
        res = requests.post(url)
