from socket import *

sockfd = socket(AF_INET,
                       SOCK_STREAM)

sockfd.bind(('0.0.0.0', 3313))

sockfd.listen(5)

while True:

    print("waiting for connect...")
    connfd,addr = sockfd.accept()
    print("Connect from ",addr)

    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        n = connfd.send(b'Receive your message')
        print("send",n,"bytes")

    connfd.close()
    print("closed")

sockfd.close()
print("closed")