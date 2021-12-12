import os
import shutil
import requests
import time
from yuzulib import stream_screen
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image, ImageDraw
import cv2

def show_screen():
    #fig = plt.figure()
    def plot(frame):
        frame = np.array(frame).astype(np.float32)
        #frame = np.array(frame)[:, :, :3]
        print(np.array(frame).shape, frame)
        plt.imshow(frame)
        plt.show()
        #cv2.imshow("image", np.array(frame).astype(np.float32))

    def callback(frame, fps):
        print("get", fps)
        plot(frame)

    stream_screen(callback, address="http://localhost:6000", fps=5, disable_warning=True)

if __name__ == "__main__":
    show_screen()