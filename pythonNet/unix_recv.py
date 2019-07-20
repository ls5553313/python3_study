 # unix_recv.py
from socket import *
import os

sock_file = "./sock_file"

if os.path.exists(sock_file):
    os.remove(sock_file)

sockfd = socket(AF_UNIX,SOCK_STREAM)

sockfd.bind(sock_file)

sockfd.listen(3)

while True:
    c,addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        else:
            print(data.decode())
            c.send(b"recieve")
    c.close()
sockfd.close()


