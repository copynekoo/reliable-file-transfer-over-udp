import argparse

# Settings
parser = argparse.ArgumentParser(
  prog='UDP Client',
  description='Download file from server client'
)

parser.add_argument('server_ip')
parser.add_argument('port')
parser.add_argument('filename')
args = parser.parse_args()

server_ip = args.server_ip
port = args.port
filename = args.filename

print(
'''Server IP: %s
Port: %s
Filename: %s'''
  % (server_ip, port, filename)
)