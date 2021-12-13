import os
import shutil
import requests
import time
from yuzulib import Client
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image, ImageDraw
import cv2

def show_screen():
    def callback(frame, fps):
        print("get", fps, frame.shape)
    client = Client(address="http://localhost:6000", disable_warning=True)
    client.run_screen(callback, fps=15, render=False)
    
if __name__ == "__main__":
    show_screen()