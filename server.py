import socket

# create server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 420))
sock.listen(1)

c = None
a = None

while c == None:
    c, a = sock.accept()
    print("listen")