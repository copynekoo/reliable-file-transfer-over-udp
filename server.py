import argparse

# Settings
parser = argparse.ArgumentParser(
  prog='UDP Server',
  description='Handles client request to download file'
)

parser.add_argument('port')
args = parser.parse_args()
port = args.port

print("Port:", port)