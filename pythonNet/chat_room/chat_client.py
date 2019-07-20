from socket import *
import sys
import os
import time

def My_UDP_client():
    sockfd = socket(AF_INET,SOCK_DGRAM)
    #sockfd.bind(('127.0.0.1',8888))
    #host = (sys.argv[1],int(sys.argv[2]))            
    pid = os.fork()
    if pid < 0:
        pass
    elif pid == 0:
        p = os.fork()
        if p == 0:
            while True:
                s,addr = sockfd.recvfrom(1024)
                print(s.decode())
        else:
            os._exit(0)
    else:
        while True:
            time.sleep(0.5)
            a = input(">>")
            if not a:
                break
            elif a == "quit":
                sockfd.sendto(a.encode(),('127.0.0.1',8888))
                break
            sockfd.sendto(a.encode(),('127.0.0.1',8888))
    sockfd.close()

My_UDP_client()