import socket
import argparse

parser = argparse.ArgumentParser(description="Client for connecting to server")
parser.add_argument("host", help="Host address of the server")
parser.add_argument("port", type=int, help="Port number of the server")

args = parser.parse_args()


obj = socket.socket()
obj.connect((args.host,args.port))
message = input("type message: ")
while message != 'q':
   obj.send(message.encode())
   data = obj.recv(1024).decode()
   print ('Received from server: ' + data)
   message = input("type message: ")
obj.close()