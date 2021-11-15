from yuzulib import Controller, Runner, Button, Screen
import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-g', '--game', help="game path: ex. /path/to/game[v0].nsp")
parser.add_argument('-d', '--dlc', help="dlc dir: ex. /path/to/dlc/")

args = parser.parse_args()
print("Game Path: {}, DLC Dir: {}".format(args.game, args.dlc))
runner = Runner(args.game, args.dlc)
runner.run()

