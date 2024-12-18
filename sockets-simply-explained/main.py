import socket

host = '127.0.0.1'
port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

while True:
    c_socket, address = server.accept()
    print(f"connected to {address}")
    message = c_socket.recv(1024).decode('utf-8')
    print(f"message from client is: {message}")
    c_socket.send(f"your message thank you".encode('utf-8'))
    c_socket.close()
    print(f"connection with {address} ended")