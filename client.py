import socket
import sys

HOST = ("localhost", 10001)
HEADER_LEN = 10

username = input("Please enter a username").encode()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(HOST)
client.setblocking(False)

header = f"{len(username):<{HEADER_LEN}}".encode()
client.send(header+username)

while True:
    print("Please write a message: ")
    msg = input().encode()

    if msg:
        msg_header = f"{len(msg):<{HEADER_LEN}}".encode()
        client.send(msg_header+msg)
        print(msg_header+msg)
    try:
        while True:

            user_header = client.recv(HEADER_LEN)  # non-blocking
            if not user_header:
                sys.exit()

            user_len = int(user_header.decode().strip())
            username = client.recv(user_len)

            msg_header = client.recv(HEADER_LEN)
            msg_len = int(msg_header.decode().strip())

            data = client.recv(msg_len).decode()
            print("New message from: {} - {}".format(username.decode(), data))
    except IOError as _ex:
        pass