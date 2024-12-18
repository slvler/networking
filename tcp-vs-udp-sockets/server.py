import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.listen()

while True:
    client, address = server.accept()
    print(f"connected to {address}")
    print(client.recv(1024).decode('utf-8'))
    client.send("client".encode('utf-8'))
    client.close()