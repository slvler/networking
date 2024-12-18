from vidstream import AudioSender
from vidstream import AudioReceiver


import threading
import socket


receiver = AudioReceiver('127.0.0.1', 9999)
receive_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender('127.0.0.1',5555)
sender_thread = threading.Thread(target=sender.start_stream)

receive_thread.start()
sender_thread.start()