# chat_room.py
# server
from socket import *
from select import select
from time import sleep


class UDP_server:
    def __init__(self):
        # self.L = []
        # self.ip = input("pls input IP:")
        # self.port = input("pls input port:")
        # self.addr = (self.ip, int(self.port))
        self.addr = ("0.0.0.0",8888)
        self.sockfd = socket(AF_INET,SOCK_DGRAM)
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.addr)

    def server_select_sock(self):
        #create a server with select and sock
        #in order to avoid IO blocking and be multiprocess
        rlist = [self.sockfd]
        wlist = []
        xlist = []

        while True:
            rs, ws, xs = select(rlist, wlist, xlist)
            for r in rs:
                    data,addr = r.recvfrom(1024)
                    print(data.decode())
                    self.sockfd.sendto(b'wtf!!!',addr)
            for w in ws:
                pass

            for x in xs:
                if x is s:
                    s.close()
        




    def server_check(self, name):
        if name not in self.L:
            return True
        else:
            return False

def main():
    c = UDP_server()
    c.server_select_sock()



if __name__ == '__main__':
    main()