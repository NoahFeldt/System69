import socket
<<<<<<< HEAD

# create server socket
=======
import threading
import os

# creates server socket
>>>>>>> yes
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

def handler(c, a):
    pass

# listens for new connections and dedicates a thread to them
def listener():
    while True:
        c, a = sock.accept()
        if c != None:
            threading.Thread(target=handler, args=(c, a), daemon=True).start()
            cons.append(c)
            adds.append(a)
            c = None

def userInterface():
    global cons
    while True:
        print(">", end="")
        command = input().lower().split(" ")
        if command[0] == "help":
            print()
            print("ADDS           Shows a list of every connected ip address.")
            print("CLS            Clears command prompt.")
            print("CONS           number of connections")
            print("HELP           Shows list of commands.")
            print("MSG            Sends a costom message to all connections.")
            print()
        elif command[0] == "cls":
            os.system("cls")
        elif command[0] == "msg":
            #print(cons)
            for i in range(len(cons)):
                cons[i].send(command[1].encode("utf-8"))

if __name__ == "__main__":
    threading.Thread(target=listener).start()
    threading.Thread(target=userInterface).start()
>>>>>>> yes
