from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)

sockfd.bind(('0.0.0.0',8888))

while True:
    data,addr = sockfd.recvfrom(1024)
    print("Recieved from %s:%s" % (addr,data.decode()))
    sockfd.sendto("Got your message".encode(),addr)

sockfd.close()