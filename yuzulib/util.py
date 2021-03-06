from pynput import mouse, keyboard
import pyautogui
import time
import os
from pathlib import Path
from enum import Enum
m = mouse.Controller()
k = keyboard.Controller()
data_path = Path(os.path.dirname(__file__)).joinpath('data/').resolve()

def click_mouse(delay: int = 0):
    m.press(mouse.Button.left)
    m.release(mouse.Button.left)
    time.sleep(delay)

def move_mouse(x: float, y: float):
    m.position = (x, y)

def press_key(key: str, delay: int = 0):
    k.press(key)
    k.release(key)
    time.sleep(delay)

def wait_screen(filepath: str, interval=1, confidence=.7):
    while True:
        location = pyautogui.locateOnScreen(filepath, confidence=confidence)
        if location != None:
            print("Reached {}!".format(filepath))
            return location
        time.sleep(interval)

def click_screen(image, interval=1, confidence=.7):
    location = None
    while True:
        location = pyautogui.locateOnScreen(image.value, confidence=confidence)
        if location != None:
            print("Reached {}!".format(image.value))
            break
        time.sleep(interval)
    point = pyautogui.center(location)
    move_mouse(point.x, point.y)
    click_mouse(delay=1)

def is_exist_screen(image, confidence=.7):
    location = pyautogui.locateOnScreen(image.value, confidence=confidence)
    if location != None:
        return True
    return False

class Image(Enum):
    INIT_YES = "{}/init_yes.png".format(str(data_path))
    INIT_SCREEN = "{}/init_screen.png".format(str(data_path))
    MENU_FILE = "{}/menu_file.png".format(str(data_path))
    INSTALL_FILES_TO_NAND = "{}/install_files_to_nand.png".format(str(data_path))
    LOAD_FILE = "{}/load_file.png".format(str(data_path))
    RESTART = "{}/restart.png".format(str(data_path))
    MENU_EMULATION = "{}/menu_emulation.png".format(str(data_path))
    OPEN_BUTTON = "{}/open_button.png".format(str(data_path))
    INSTALL_BUTTON = "{}/install_button.png".format(str(data_path))
    OK_BUTTON = "{}/ok_button.png".format(str(data_path))
    YUZU_SCREEN = "{}/yuzu_screen.png".format(str(data_path))
    TOP_BAR = "{}/top_bar.png".format(str(data_path))
    BOTTOM_BAR = "{}/bottom_bar.png".format(str(data_path))