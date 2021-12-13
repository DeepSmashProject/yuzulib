import os
import shutil
import requests
import time
from yuzulib import Client, Button
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image, ImageDraw
import cv2

def show_screen():
    client = Client(address="http://localhost:6000", disable_warning=True)
    def callback(frame, fps):
        print("get", fps, frame.shape)
        client.press([Button.BUTTON_A], hold=True, sec=0.02)
    client.run_screen(callback, fps=15, render=True, width=500, height=300)

def run_game_test():
    game_path = "/workspace/games/SSBU/'Super Smash Bros Ultimate [v0].nsp'"
    dlc_dir = "/workspace/games/SSBU/DLC"
    client = Client(address="http://localhost:6000", disable_warning=True)
    client.run_game(game_path, dlc_dir)

if __name__ == "__main__":
    #show_screen()
    run_game_test()
    # TODO: async callback
    # TODO: RunnerView