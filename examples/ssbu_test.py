from yuzulib import Runner, Button, Screen
from yuzulib.game.ssbu import UltimateController, Stage, Fighter
import time
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-g', '--game', help="game path: ex. /path/to/game[v0].nsp")
parser.add_argument('-d', '--dlc', help="dlc dir: ex. /path/to/dlc/")

args = parser.parse_args()
print("Game Path: {}, DLC Dir: {}".format(args.game, args.dlc))
if args.game == "" or args.dlc == "":
    print("Invalid argument")
    os.exit(1)

def callback(frame, fps):
    print("callback!", frame.shape, fps)
screen = Screen(callback, fps=60)
screen.run()

controller = UltimateController()
training_mode = controller.mode.training
config = {
    "stage": Stage.STAGE_HANENBOW, 
    "player": {"fighter": Fighter.FIGHTER_MARIO.name, "color": 0}, 
    "cpu": {"fighter": Fighter.FIGHTER_DONKEY_KONG.name, "color": 0, "level": 9},
    "setting": {"quick_mode": True, "cpu_behavior": "cpu", "diable_combo_display": True}
}
training_mode.start(config)