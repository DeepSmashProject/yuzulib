
import threading
from flask import Flask, Response,stream_with_context, request
from flask_cors import CORS
from .controller import Controller
import json
from .enums import Button
from .screen import Screen
import time
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

@app.route("/screen", methods=['GET'])
def get_screen():
    # curl -X GET 'localhost:6000/screen'
    event = threading.Event()
    screen_data = {"frame": None, "fps": 0}
    def callback(frame, fps):
        screen_data["frame"] = frame
        screen_data["fps"] = fps
        event.set()

    screen = Screen(callback, fps=60)
    screen.run()
    def generate():
        try:
            while True:
                event.wait()
                event.clear()
                yield json.dumps(screen_data)
                
        except GeneratorExit:
            print('closed')
            return Response("Exit"), 420
        except Exception as err:
            print('error', err)
            return Response("Error: {}".format(err)), 422
    return Response(stream_with_context(generate())), 200

def run_server():
    app.debug = False
    app.run(host='0.0.0.0', port=6000)

if __name__ == "__main__":
    run_server()