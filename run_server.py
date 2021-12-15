import argparse
from yuzulib.server import Server, ControllerView, RunnerView, ScreenView

parser = argparse.ArgumentParser(description='')
parser.add_argument('--host')
parser.add_argument('--port')

args = parser.parse_args()
print("Running Yuzu Server at {}:{}".format(args.host, args.port))
server = Server(host=str(args.host), port=int(args.port), views=[ControllerView, RunnerView, ScreenView])
server.run()