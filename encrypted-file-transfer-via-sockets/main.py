from Crypto.Cipher import AES
import os
import socket

key = b"TheJohnDoeKey"
nonce = b"TheJohnDoeNce"

cipher = AES.new(key, AES.MODE_EAX, nonce)
cipherText = cipher.encrypt(b"Hello world")

print(cipherText)

cipher = AES.new(key, AES.MODE_EAX, nonce)
print(cipher.decrypt(cipherText))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

file_size = os.path.getsize("file")

with open ("file", "rb") as f:
    data = f.read()


encrypted = cipher.encrypt(data)
client.send("file.txt".encode())
client.send(str(file_size).encode())
client.sendall(encrypted)
client.send(b"<end>")

client.close()