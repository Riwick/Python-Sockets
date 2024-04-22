import socket

HOST = ("localhost", 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
client.setblocking(False)

print(client.gettimeout())

data = "Hello world!"*1024*1024*5
sent = client.send(data.encode())
print(sent, len(data))
