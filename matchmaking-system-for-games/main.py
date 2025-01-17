import socket

tries = int(input("Tries: "))
max_number = int(input("Maximum number: "))
role = int(input("Role: "))


config_string = f"{tries}-{max_number}-{role}"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))

client.send(config_string.encode())

print(client.recv(1024).decode())
client.send(input().encode())


while True:
    message = client.recv(1024).decode()
    print(message)
    if "tries" in message or "lost" in message or "ınvalid" in message:
        break
    if role == "guesser":
        client.send(input().encode())
