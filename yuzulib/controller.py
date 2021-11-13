from contextlib import ExitStack
from typing import List
import pyautogui
from .enums import Button
import time
from pynput.keyboard import Controller as Con
class Controller:
    def __init__(self):
        self._hold_buttons = []
        # blank push for focus keyboard
        self.keyboard = Con()
        self.press(Button.BUTTON_MODIFIER)

    def press(self, button: Button, sec=None):
        self.keyboard.press(button.value)
        if sec != None:
            time.sleep(sec)
        self.keyboard.release(button.value)

    def multi_press(self, buttons: List[Button], sec=None):
        if len(buttons) == 0:
            return
        with ExitStack() as stack:
            for i, button in enumerate(buttons):
                if i == len(buttons)-1:
                    break
                stack.enter_context(self.keyboard.pressed(button.value))
            self.press(buttons[len(buttons)-1], sec)

    def hold(self, button: Button):
        pyautogui.keyDown(button.value)
        self._hold_buttons.append(button)

    def hold_buttons(self):
        return self._hold_buttons

    def release(self, button: Button):
        pyautogui.keyUp(button.value)

if __name__ == '__main__':
    controller = Controller()
    controller.press(Button.BUTTON_A)
    controller.multi_press([Button.BUTTON_A, Button.BUTTON_C_DOWN])