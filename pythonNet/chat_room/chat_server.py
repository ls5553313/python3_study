from UDP_server import *
from socket import *
import sys
import os
import time

class Chat_server(UDP_server):
    def __init__(self):
        super().__init__()
        self.dict = {}

    def send_to_all(self,data):
        for x in list(self.dict.keys()):
                self.sockfd.sendto(data.encode(), x)

    def write_to_namebook(self):
        file = open("namebook.txt",'w')
        L = []
        for x in self.dict.keys():
            L.append(str(x) + "\n")
        file.writelines(L)



    def myexit(self, data, addr):
        if data.decode() == "quit":
            SendAllData = str(self.dict[addr]) + 'has left the Chatroom' 
            self.send_to_all(SendAllData)
            print(SendAllData)
            del self.dict[addr]
            return True
        else:
            return False

    def Addr_Check(self, addr, data):
        if addr in list(self.dict.keys()):
            SendAllData = str(self.dict[addr]) + ':' + data.decode()
            self.send_to_all(SendAllData)
            print(SendAllData)
        else:
            make_name = "pls input a name: "
            self.sockfd.sendto(make_name.encode(), addr)
            name, addr = self.sockfd.recvfrom(1024)
            print(name, addr)
            while self.Name_Check(name.decode()):
                make_name = "pls input another name: "
                self.sockfd.sendto(make_name.encode(), addr)
                name, addr = self.sockfd.recvfrom(1024)
            self.dict[addr] = name.decode()
            print(self.dict)
            self.write_to_namebook()
            SendAllData = str(self.dict[addr]) + 'has entered the Chatroom' 
            self.send_to_all(SendAllData)
            print(SendAllData)

    def Name_Check(self, name):
        l = []
        for x in list(self.dict.keys()):
            l.append(self.dict[x])
        if name in l:
            return(True)
        else:
            return(False)

    def server_select(self):
        # create a server with select and sock
        # in order to avoid IO blocking and be multiprocess
        rlist = [self.sockfd]
        wlist = []
        xlist = []

        while True:
            rs, ws, xs = select(rlist, wlist, xlist)
            for r in rs:
                data, addr = r.recvfrom(1024)
                if self.myexit(data, addr):
                    continue
                self.Addr_Check(addr, data)
            for w in ws:
                pass

            for x in xs:
                if x is s:
                    s.close()

    def RecvAndSend(self):
        pid = os.fork()
        if pid < 0:
            pass
        elif pid == 0:
            p = os.fork()
            if p == 0:
                while True:
                    time.sleep(0.5)
                    a = input(">>")
                    data = 'server:' + a
                    print(data)
                    file = open("namebook.txt","r")
                    for x in file.readlines():
                        str1 = x[1:-2]
                        ip,port = str1.split(",")
                        addr = (str(ip[1:-1]),int(port))
                        print(addr)
                        self.sockfd.sendto(data.encode(),addr)
            else:
                os._exit(0)
        else:
            pid2, status = os.wait()
            self.server_select()

chat = Chat_server()
chat.RecvAndSend()


