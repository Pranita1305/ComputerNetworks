import socket
import argparse
from multiprocessing import Process
import os

host = "127.0.0.1"

# Parse port from command line
parser = argparse.ArgumentParser(description="Multi-process server for connecting to clients")
parser.add_argument("port", type=int, help="Port number of the server")
args = parser.parse_args()

def handle_client(conn, addr):

    print(f"[PID {os.getpid()}] Handling connection from: {addr}")
    print("Connection from:", addr)
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        data_rev = ""
        for i in range(len(data) - 1, -1, -1):
            data_rev += data[i]
        print (" from client: " + str(data))
        conn.send(data_rev.encode())
    conn.close()

# Main server loop
def main():
    server = socket.socket()
    server.bind((host, args.port))
    server.listen()
    print(f"Server listening on {host}:{args.port}")

    while True:
        conn, addr = server.accept()
        # Spawn a new process for each client
        client_process = Process(target=handle_client, args=(conn, addr))
        client_process.start()
        conn.close()  # Close parent copy

if __name__ == "__main__":
    main()