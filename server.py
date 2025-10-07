import argparse
import socket

# Settings
parser = argparse.ArgumentParser(
  prog='UDP Server',
  description='Handles client request to download file'
)

parser.add_argument('port')
args = parser.parse_args()
port = args.port

print("Port:", port)

server_folder = './server/'
buffer_size = 1024

# Response to client
server_ip = '127.0.0.1'
port = int(port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((server_ip, port))

print("Server is running and waiting for request.")
while True:
  data, addr = sock.recvfrom(buffer_size)
  fileName = data.decode('utf-8')
  print("Requested file:", fileName)

  try:
    a = server_folder + fileName

    with open(a, 'rb') as file:
      print("File exists and is ready to read")
      sock.sendto(b"1", addr)
      data = file.read(buffer_size)
      sock.sendto(data, addr)
      while data:
        data = file.read(buffer_size)
        sock.sendto(data, addr)

      print(fileName, "reached EoF")
  except FileNotFoundError:
    print("File does not exist")
    sock.sendto(b"0", addr)