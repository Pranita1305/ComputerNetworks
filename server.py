import socket
import argparse
host = "127.0.0.1"
# port = 5001

parser = argparse.ArgumentParser(description="Server for connecting to Client")
parser.add_argument("port", type=int, help="Port number of the server")

args = parser.parse_args()

server = socket.socket()
server.bind((host,args.port))
server.listen()
conn, addr = server.accept()
print ("Connection from: " + str(addr))
while True:
   data = conn.recv(1024).decode()
   if not data:
      break
   data_rev=""
   for i in range(len(data)-1,-1,-1):
       data_rev+=data[i]
       
#    print (" from client: " + str(data_rev))
#    data = input("type message: ")
   conn.send(data_rev.encode())
conn.close()