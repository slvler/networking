import socket

HOST = '127.0.0.1'
PORT = 9000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send("hello world".encode('utf-8'))
print(socket.recv(1024))