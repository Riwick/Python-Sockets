import socket
import select

HOST = ("localhost", 10000)
HEADER_LEN = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(HOST)
s.listen()

print("I'm listening connections")

sockets_list = [s]
client_list = {}


def receive_msg(client: socket.socket):
    try:
        msg_header = client.recv(HEADER_LEN)
        if not msg_header:
            return False

        msg_len = int(msg_header.decode("utf-8").strip())

        return {
            "header": msg_header,
            "data": client.recv(msg_len).decode("utf-8")
        }
    except:
        return False


while True:
    rs, _, xs = select.select(sockets_list, [], sockets_list)
    for _socket in rs:
        if _socket == s:
            client, addr = s.accept()

            user = receive_msg(client)
            if user is False:
                continue
            sockets_list.append(client)
            client_list[client] = user

            print("New connection from {} with data {}".format(addr, user["data"]))
        else:
            client, addr = s.accept()

            msg = receive_msg(client)
            if msg is False:
                print("New connection from {} has been interrupted".format(addr))

                sockets_list.remove(_socket)
                del client_list[_socket]

                continue

            user = client_list[_socket]

            for client in client_list:
                if client is not _socket:
                    client.send("New message from {} is {}".format(user["data"], msg["data"]).encode())

    for _socket in xs:
        sockets_list.remove(_socket)
        del client_list[_socket]

