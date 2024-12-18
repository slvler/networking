import socket
import pickle

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = load_iris()
X,y = data.data, data.target

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 9999))

server.listen(1)

while True:
    print("for connection...")
    client, addr = server.accept()

    try:
        print('connected')

        data = b''
        while True:
            chunk = client.recv(4096)
            if not chunk:
                break
            data += chunk

        received_object = pickle.loads(data)
        print(f'Received: {received_object}')

        print(f'Accurancy: {received_object.score(X,y)}')
    finally:
        client.close()