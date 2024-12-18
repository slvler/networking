import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))


client.send("server!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
client.send("server-by!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))