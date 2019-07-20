from socket import *

sockfd = socket()

sockfd.connect(('127.0.0.1', 8888))

while True:
    a = input("send>>")
    if not a:
        break
    sockfd.send(a.encode())
    print(sockfd.recv(1024).decode())

sockfd.close()