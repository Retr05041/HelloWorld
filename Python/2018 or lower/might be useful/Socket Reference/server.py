import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8888))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print("Connection from " + str(address) + " has been established")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
