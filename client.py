import socket

# creates socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connects to server
def connect():
    while True:
        try:
            sock.connect(("localhost", 420))
            break
        except ConnectionRefusedError:
            print("connection failed!")

connect()

print("Im in!")

while True:
    try:
        print(sock.recv(1024))
    except ConnectionResetError:
        connect()