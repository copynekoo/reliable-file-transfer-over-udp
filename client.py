import argparse

parser = argparse.ArgumentParser(
  prog='UDP Client',
  description='Download file from server client'
)

parser.add_argument('server_ip')
parser.add_argument('port')
parser.add_argument('filename')
args = parser.parse_args()
print(args.server_ip, args.port, args.filename)