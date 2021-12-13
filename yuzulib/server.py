
import sys
import threading
from flask import Flask, Response,stream_with_context, request
from flask_cors import CORS
from .controller import Controller
import json
from .enums import Button
from .screen import Screen
from .runner import Runner
import time
import numpy as np
import requests
import cv2
from flask_classful import FlaskView, route


class ControllerView(FlaskView):
    controller = Controller()
    controller.run()
    @route('/press',methods=["POST"])
    def press(self):
        # curl -X POST -d '{"buttons": ["BUTTON_A"]}' 'localhost:6000/controller/press?hold=True&sec=0&wait=0'
        req_data = json.loads(request.get_data())
        hold = request.args.get('hold', False)
        hold = True if hold == "True" else False
        sec = float(request.args.get('sec', 0))
        wait = float(request.args.get('wait', 0))
        if "buttons" not in req_data.keys():
            return Response("ERROR: {} argument is not exist".format("buttons")), 400
        buttons = []
        for bt in req_data["buttons"]:
            if not bt in Button.__members__:
                return Response("ERROR: {} argument is not exist".format(bt)), 400
            buttons.append(Button[bt])
        #print("test", buttons, hold, sec, wait)
        self.controller.press(buttons, hold=hold, sec=sec, wait=wait)
        return Response("OK"), 200

class ScreenView(FlaskView):
    screen_data = {"frame": None, "fps": 0}
    screen_flag = {"running": False}

    @route('/',methods=["POST"])
    def run(self):
        # curl -X POST 'localhost:6000/screen/?fps=60&disable_warning=true'
        if self.screen_flag["running"]:
            return Response("Error: screen is already running"), 400
        fps = int(request.args.get('fps', 60))
        disable_warning = request.args.get('disable_warning', False)
        disable_warning = True if disable_warning == "true" else False
        def callback(frame, fps):
            self.screen_data["frame"] = frame
            self.screen_data["fps"] = fps

        screen = Screen(callback, fps=fps, disable_warning=disable_warning)
        screen.run()
        self.screen_flag["running"] = True
        return Response("OK"), 200

    @route('/',methods=["GET"])
    def get(self):
        # curl -X GET 'localhost:6000/screen/?width=256&height=256'
        if not self.screen_flag["running"]:
            return Response("Error: screen is not running"), 400
        width = int(request.args.get('width', 256))
        height = int(request.args.get('height', 256))
        frame = self.screen_data["frame"]
        width = width if width <= frame.shape[1]-1 else frame.shape[1]-1
        height = height if height <= frame.shape[0]-1 else frame.shape[0]-1
        frame = np.array(frame)[:, :, :3].tolist()
        frame = cv2.resize(np.array(frame).astype(np.float32), (width, height)).tolist()
        frame = cv2.cvtColor(np.array(frame).astype(np.uint8), cv2.COLOR_BGR2RGB).tolist()
        screen_data = {"frame": frame, "fps": self.screen_data["fps"]}
        
        return Response(json.dumps(screen_data)), 200

class RunnerView(FlaskView):
    runner = Runner()
    @route('/run_game',methods=["POST"])
    def run_game(self):
        # curl -X POST -d '{"dlc_dir": /path/to/dlc_dir, "game_path": /path/to/game_path}' 'localhost:6000/runner/run_game'
        req_data = json.loads(request.get_data())
        for key in ["dlc_dir", "game_path"]:
            if key not in req_data.keys():
                return Response("ERROR: {} argument is not exist".format(key)), 400
        self.runner.run_game(req_data["game_path"], req_data["dlc_dir"])

    @route('/reset_game',methods=["POST"])
    def reset_game(self):
        # curl -X POST 'localhost:6000/runner/reset_game'
        self.runner.reset_game()

class Server:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    def run(self):
        app = Flask(__name__)
        CORS(app) #Cross Origin Resource Sharing
        ControllerView.register(app)
        ScreenView.register(app)
        RunnerView.register(app)
        app.debug = False
        app.run(host=self.host, port=self.port)

if __name__ == '__main__':
    server = Server(host='0.0.0.0', port=6000)
    server.run()