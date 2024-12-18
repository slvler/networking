import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()


while True:
    client, addr = server.accept()
    client.send("Hello world".encode())
    print(client.recv(1024).decode())
    client.close()