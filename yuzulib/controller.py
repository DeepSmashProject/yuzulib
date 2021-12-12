from contextlib import ExitStack
from typing import List
from cv2 import mulSpectrums
import pyautogui
from .enums import Button
import threading
import time
from pynput.keyboard import Controller as Con
class Controller:
    def __init__(self):
        self.control_event = threading.Event()
        self.kill_event = threading.Event()
        self.unhold_event = threading.Event()
        self.data = {"buttons": [], "hold": False, "sec": 0}
        # blank push for focus keyboard
        self.keyboard = Con()
        self.run()
        self.press([Button.BUTTON_MODIFIER])

    def run(self):
        thread = threading.Thread(target=self._control)
        thread.start()
        time.sleep(1)

    def press(self, buttons, hold=False, sec=0, wait=0):
        if self.data["hold"]:
            if buttons == self.data["buttons"]:
                if not hold:
                    self.unhold_event.set()
                else:
                    return
            else:
                self.unhold_event.set()
        self.data = {"buttons": buttons, "hold": hold, "sec": sec}
        self.control_event.set()
        time.sleep(wait)

    def _control(self):
        while True:
            self.control_event.wait()
            self.control_event.clear()
            if self.kill_event.is_set():
                break
            self._press()

    def _press(self):
        print(self.data)
        buttons = self.data["buttons"]
        if len(buttons) == 0:
            return
        with ExitStack() as stack:
            for i, button in enumerate(buttons):
                if i == len(buttons)-1:
                    break
                stack.enter_context(self.keyboard.pressed(button.value))
            last_button = buttons[len(buttons)-1]
            self.keyboard.press(last_button.value)
            if self.data["hold"]:
                self.unhold_event.wait()
                self.unhold_event.clear()
                self.keyboard.release(last_button.value)
            else:
                if self.data["sec"] != None:
                    time.sleep(self.data["sec"])
                self.keyboard.release(last_button.value)

    def close(self):
        time.sleep(1)
        self.unhold_event.set()
        self.kill_event.set()
        self.control_event.set()

if __name__ == '__main__':
    controller = Controller()
    controller.run()
    controller.press([Button.BUTTON_A, Button.BUTTON_C_DOWN])
    controller.close()