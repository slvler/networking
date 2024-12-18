import socket

client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
client.connect(("::1", 9999))

client.send("client".encode())
print(client.recv(1024).decode())