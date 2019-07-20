from socket import *

sockfd = socket()

sockfd.bind(('0.0.0.0',8000))

sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

sockfd.listen(5)

while True:

    print("waiting for connect...")
    connfd,addr = sockfd.accept()
    print("Connect from ",addr)

    file = open("document1.png","wb")
    while True:
        data = connfd.recv(1024)
        if data:
            print("********************************")
        else:
            print("NONE")
        if not data:
            break
        file.write(data)
    
    file.close()


    connfd.close()
    print("closed")

sockfd.close()
print("closed")