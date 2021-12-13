
import sys
import threading
from flask import Flask, Response,stream_with_context, request
from flask_cors import CORS
from .controller import Controller
import json
from .enums import Button
from .screen import Screen
import time
import numpy as np
import requests
app = Flask(__name__)
CORS(app) #Cross Origin Resource Sharing

controller = Controller()
controller.run()

@app.route("/controller/press", methods=['POST'])
def press():
    # curl -X POST -d '{"buttons": ["BUTTON_A"]}' 'localhost:6000/controller/press?hold=true&sec=0&wait=0'
    req_data = json.loads(request.get_data())
    hold = request.args.get('hold', False)
    hold = True if hold == "true" else False
    sec = float(request.args.get('sec', 0))
    wait = float(request.args.get('wait', 0))
    if "buttons" not in req_data.keys():
        return Response("ERROR: {} argument is not exist".format("buttons")), 400
    buttons = []
    for bt in req_data["buttons"]:
        if not bt in Button.__members__:
            return Response("ERROR: {} argument is not exist".format(bt)), 400
        buttons.append(Button[bt])
    print("test", buttons, hold, sec, wait)
    controller.press(buttons, hold=hold, sec=sec, wait=wait)
    return Response("OK"), 200


screen_data = {"frame": None, "fps": 0}
screen_flag = False

@app.route("/screen", methods=['POST'])
def run_screen():
    # curl -X POST 'localhost:6000/screen?fps=60&disable_warning=true'
    global screen_flag
    if screen_flag:
        return Response("Error: screen is already running"), 400
    fps = int(request.args.get('fps', 60))
    disable_warning = request.args.get('disable_warning', False)
    disable_warning = True if disable_warning == "true" else False
    def callback(frame, fps):
        screen_data["frame"] = np.array(frame)[:100,:100].tolist()
        screen_data["fps"] = fps

    screen = Screen(callback, fps=fps, disable_warning=disable_warning)
    screen.run()
    screen_flag = True
    return Response("OK"), 200

@app.route("/screen", methods=['GET'])
def get_screen():
    # curl -X GET 'localhost:6000/screen'
    global screen_flag
    if not screen_flag:
        return Response("Error: screen is not running"), 400
    
    return Response(json.dumps(screen_data)), 200

def run_server():
    app.debug = False
    app.run(host='0.0.0.0', port=6000)

def stream_screen(callback, address="http://localhost:6000", fps=15, disable_warning=False):
    print("run screen")
    url = '{}/screen'.format(address)
    if disable_warning:
        url = '{}/screen?disable_warning=true'.format(address)
    res = requests.post(url)
    time.sleep(1)
    start = time.time()
    while True:
        url = '{}/screen'.format(address)
        res = requests.get(url)
        elapsed_time = time.time() - start
        target_elapsed_time = 1/fps
        if target_elapsed_time < elapsed_time:
            if not disable_warning:
                print("warning: low fps {}".format(1/elapsed_time))
        else:
            time.sleep(target_elapsed_time-elapsed_time)
            elapsed_time = time.time() - start
        if res.status_code == 400:
            print("Error")
            break
        start = time.time()
        callback(res.json()["frame"], 1/elapsed_time)

if __name__ == "__main__":
    run_server()