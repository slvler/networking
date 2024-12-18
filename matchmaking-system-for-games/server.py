import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))
server.listen()

connected_clients = []

def handle_match(c1, c2):
    tries, max_num = c1[1].split("-")
    tries, max_num = int(tries), int(max_num)

    if c1[2] != "decider":
        c1, c2 = c2, c1

    c1[0].send("Enter the number to be guess". encode())
    number = int(c1[0].recv(1024).decode)

    if number > max_num:
        c1[0].send("ınvalid range".encode())
        c2[0].send("your partner messed up ınvalid ranger".encode())
        c1[0].close()
        c2[0].close()
    else:
        guessed = False
        try_counter = 0
        c2[0].send("enter".encode())
        while not guessed:
            try_counter += 1
            guess = int(c2[0].recv(1024).decode())


def handle_client(c):
    c.send("enter matching string".encode())

    config_string = client.recv(1024).decode()

    config = config_string[:config_string.rfind("-")]
    role = config_string[config_string.rfind("-")+1:]
    found_match = False

    matching_string = client.recv(1024).decode()
    found_match = False
    for i in range(len(connected_clients)):
        if connected_clients[i][1] == matching_string:
            threading.Thread(target=handle_match, args=(c, connected_clients[i][0])).start()
            del connected_clients[i]
            found_match = True

    if not found_match:
        connected_clients.append((c, matching_string))


while True:
    client, addr = server.accept()
    threading.Thread(target=handle_client, args=(client,)).start()