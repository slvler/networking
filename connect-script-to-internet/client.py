import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost"))

print(client.recv(1024).decode())
client.send("Hey server".encode())