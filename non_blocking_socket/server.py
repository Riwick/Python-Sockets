import socket

HOST = ("localhost", 10000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(HOST)
server.listen()

print("Listening")

while True:
    client, addr = server.accept()
    print("New connection from {}".format(addr))

    data = client.recv(1024)
    while data:
        print(data)
        data = client.recv(1024)

    print(data.decode())
    print("All data has been received")
    client.close()
