from contextlib import ExitStack
from typing import List
import pyautogui
import time
import subprocess
import threading
import os
from pathlib import Path
from .util import click_mouse, press_key, move_mouse, wait_screen, click_screen, Image, is_exist_screen
from pynput import mouse, keyboard
import glob
class Runner:
    def __init__(self):
        self.data_path = Path(os.path.dirname(__file__)).joinpath('data/').resolve()

    def run_game(self, game_path: str, dlc_dir: str):
        self._click_init_yuzu_help_menu()
        self._install_dlc(dlc_dir)
        self._install_and_start_game(game_path)
        time.sleep(5)
        self._restart_game()

    def reset_game(self):
        self._restart_game()

    def _click_init_yuzu_help_menu(self):
        ########## Init Yuzu Help Menu ##########
        if is_exist_screen(Image.INIT_SCREEN):
            click_screen(Image.INIT_YES)

    def _install_dlc(self, dlc_dir):
        print("Start Installing DLC")
        files = glob.glob(dlc_dir + "/*.nsp")
        dlc_str = ""
        for file in files:
            dlc_str += str('"') + file + str('"')
            dlc_str += " "
        time.sleep(1)
        
        ######## Install DLC File #########
        # Click Files menu
        click_screen(Image.MENU_FILE)
        #move_mouse(226, 125)
        #click_mouse(delay=0.1)
        # Click Install Nand
        click_screen(Image.INSTALL_FILES_TO_NAND)
        #move_mouse(226, 153)
        #click_mouse(delay=1)
        # Type dlc files
        for s in dlc_str:
            press_key(s, delay=0.001)
        time.sleep(1)
        # Click Open Button
        click_screen(Image.OPEN_BUTTON)
        click_screen(Image.OPEN_BUTTON)

        click_screen(Image.INSTALL_BUTTON)

        print("Installing {} dlc files.".format(len(files)))
        click_screen(Image.OK_BUTTON)
        print("Finished Install {} DLC Files".format(len(files)))
    
    def _install_and_start_game(self, game_path):
        print("Start Installing Game")
        click_screen(Image.MENU_FILE)
        click_screen(Image.LOAD_FILE)

        # in File Select
        # ex_str = "/workspace/games/SSBU/Super Smash Bros Ultimate [v0].nsp"
        for s in game_path:
            press_key(s)
        time.sleep(1)
        
        # Click File Open Button
        click_screen(Image.OPEN_BUTTON)
        click_screen(Image.OPEN_BUTTON)
        
        print("Installing game file: {}.".format(game_path))
    
    def _restart_game(self):
        print("Reset Game")
        # Click Emulator menu
        click_screen(Image.MENU_EMULATION)
        # Reset Game
        click_screen(Image.RESTART)

    
if __name__ == '__main__':
    runner = Runner("", "")
    runner.run()