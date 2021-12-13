import argparse
from yuzulib import Server

parser = argparse.ArgumentParser(description='このプログラムの説明（なくてもよい）')
parser.add_argument('--host')
parser.add_argument('--port')

args = parser.parse_args()
print("Running Server at {}:{}".format(args.host, args.port))
server = Server(host=str(args.host), port=int(args.port))
server.run()