# unix_send.py
from socket import *
import os

sock_file = "./sock_file"

sockfd = socket(AF_UNIX,SOCK_STREAM)

sockfd.connect(sock_file)

while True:
    msg = input('send>>')
    if msg:
        sockfd.send(msg.encode())
        print(sockfd.recv(1024).decode())
    else:
        break
sockfd.close()
