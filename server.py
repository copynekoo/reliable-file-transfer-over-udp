import argparse

parser = argparse.ArgumentParser(
  prog='UDP Server',
  description='Handles client request to download file'
)

parser.add_argument('port')
args = parser.parse_args()
print(args.port)