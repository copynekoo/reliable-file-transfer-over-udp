import argparse
import socket
from pathlib import Path

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

# Directory where downloaded files are stored
client_folder = './client/'
Path(client_folder).mkdir(parents=True, exist_ok=True) # Create client folder if the folder does not exist

# Request to server
port = int(port)
address = (server_ip, port)
fileName = bytes(filename, 'utf-8')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Request to server to check if file exists
sock.sendto(fileName, address)
decoded_fileName = fileName.decode('utf-8')
print("Requesting file:", decoded_fileName)
data, addr = sock.recvfrom(1024)
exist = int(data)

if exist:
    print("File is exist and initiating download.")
    fileName = fileName.decode('utf-8')
    downloaded_file = open(client_folder + fileName, "wb")
    while True:
        data, addr = sock.recvfrom(1024)
        if data:
            downloaded_file.write(data)
        if not data:
            downloaded_file.close()
            break

    print("File is downloaded.")
else:
    print("File does not exist.")