import socket

HOST = ("localhost", 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
print("Connected to", HOST)

sent = 0
request = b" GET / HTTP1.1\r\nHost:localhost:1000\r\n\r\n"
# while sent < len(request):  # socket.sendall()
#     sent = sent + client.send(request[sent:])

client.sendall(request)

print("Sent msg")
