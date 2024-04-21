import socket

HOST = ("localhost", 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
print("Connected to", HOST)

msg = ""
while True:
    data = client.recv(8)
    msg += data.decode("utf-8")
    if not len(data):
        break

print(msg)
