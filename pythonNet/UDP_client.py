from socket import *
import sys

sockfd = socket(AF_INET,SOCK_DGRAM)

#sockfd.bind(('127.0.0.1',8888))
#host = (sys.argv[1],int(sys.argv[2]))

while True:
    a = input("send>>")
    if not a:
        break
    sockfd.sendto(a.encode(),('127.0.0.1',8888))
    s,addr = sockfd.recvfrom(1024)
    print("Recieved from %s:%s" % (addr,s.decode()))


sockfd.close()