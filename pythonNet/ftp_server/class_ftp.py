import os,sys
from socket import *
import signal

class FtpServer():

    def __init__(self,host="",port=8888):
        self.s = socket()
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.s.bind((host,port))
        self.s.listen(5)
        signal.signal(signal.SIGCHLD,signal.SIG_IGN)
        #print("进程%d等待客户端连接"%os.getpid())
        while True:
            try:
                self.client, self.client_addr = self.s.accept()
                print("connected:", elf.client_addr)
            except KeyboardInterrupt:
                sys.exit()
            except Exception as e:
                print(e)
                continue

            pid = os.fork()

            if pid == 0:
                self.s.close()
                child_process(self.client)
            else:
                self.client.close()
                continue


    def child_process(self):
    #print("处理子进程的请求:",c.getpeername())
        try:
            while True:
                data = self.client.recv(4096)
                #print(data)
                if not data:
                    break
                data_handle(data)
        except (KeyboardInterrupt,SystemError):
            sys.exit("server stop")
        except Exception as e:
            print(e)
        self.client.close()
        sys.exit()

    def data_handle(self,data):

        if data == "1":
            dirs = os.listdir("./")
            self.client.send(str(dirs).encode())
    
        elif data == "2":
            #dirs = os.listdir("./")
            #c.send(str(dirs).encode())
            file = open("document1.png","rb")
            while True:
                file_data = file.read(4096)
                #data_send = "2 ".encode() + file_data
                c.send(file_data)
                if len(file_data) < 4096:
                    break
            file.close()

        elif data == i.encode():
            # dirs = os.listdir("./")
            # c.send(str(dirs).encode())
            # filename_save = data[3:]
            file_123 = open("document333.png","wb")
        else:
            while True:
                data_recv = data
                #data_save = data_recv.decode()[3:].encode()
                file_123.write(data_recv)
                if len(data_recv) < 4096:
                    break
            file.close()
