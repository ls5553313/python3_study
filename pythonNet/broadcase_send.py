from socket import *
from time import sleep

dest = ('192.168.31.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto("asdadada".encode(),dest)

s.close()