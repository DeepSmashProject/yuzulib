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
        self.hold_buttons = []
        self.hold_event = threading.Event()
        self.holding = False
        # blank push for focus keyboard
        self.keyboard = Con()
        self.press(Button.BUTTON_MODIFIER)

    def _check_hold(self, hold, buttons: List[Button]):
        if self.hold_buttons == buttons:
            return False
        else:
            if self.holding:
                self.hold_event.set()
            if hold:
                self.hold_buttons = buttons
            else:
                self.hold_buttons = []
            return True

    def _press(self, button: Button, hold=False, sec=None, wait=None):
        self.keyboard.press(button.value)
        if hold:
            self.holding = True
            self.hold_event.wait()
            self.hold_event.clear()
            self.holding = False
            self.keyboard.release(button.value)
        else:
            if sec != None:
                time.sleep(sec)
            self.keyboard.release(button.value)

    def press(self, button: Button, hold=False, sec=None, wait=None):
        change = self._check_hold(hold, [button])
        if change:
            thread = threading.Thread(target=self._press, args=(button, hold, sec, wait))
            thread.start()

    def _multi_press(self, buttons: List[Button], hold=False, sec=None, wait=None):
            if len(buttons) == 0:
                return
            with ExitStack() as stack:
                for i, button in enumerate(buttons):
                    if i == len(buttons)-1:
                        break
                    stack.enter_context(self.keyboard.pressed(button.value))
                self._press(buttons[len(buttons)-1], hold=hold, sec=sec, wait=wait)

    def multi_press(self, buttons: List[Button], hold=False, sec=None, wait=None):
        change = self._check_hold(hold, buttons)
        if change:
            thread = threading.Thread(target=self._multi_press, args=(buttons, hold, sec, wait))
            thread.start()
        if wait != None:
            time.sleep(wait)

    def release(self, button: Button):
        pyautogui.keyUp(button.value)

    def close(self):
        self.hold_event.set()

if __name__ == '__main__':
    controller = Controller()
    controller.press(Button.BUTTON_A)
    controller.multi_press([Button.BUTTON_A, Button.BUTTON_C_DOWN])