import pickle
import socket

HOST = ("localhost", 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
print("Connected to", HOST)

