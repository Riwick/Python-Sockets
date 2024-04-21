import socket

HOST = ("localhost", 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(HOST)
s.listen()

print("I'm listening connections")

while True:
    conn, addr = s.accept()
    print("Connected - ", addr)
    res = b"Hello, my friend!"  # encode(fmt)
    conn.send(res)

    conn.close()

