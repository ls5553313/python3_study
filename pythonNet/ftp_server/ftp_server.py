import os,sys
from socket import *
import signal

def download(c,file_name):
    file = open(file_name,"rb")
    while True:
        file_data = file.read(4096)
        #data_send = "2 ".encode() + file_data
        c.send(file_data)
        if len(file_data) < 4096:
            break
    file.close()

def upload(data,c):
    filename = data[3:].decode() + "upload"
    file_123 = open(filename,"wb")
    while True:
        data_recv = c.recv(4096)
        #data_save = data_recv.decode()[3:].encode()
        file_123.write(data_recv)
        if len(data_recv) < 4096:
            break
    file_123.close()

def data_handle(data,c):
    if data == b"1":
        dirs = os.listdir("./")
        c.send(str(dirs).encode())
    
    elif data[0:3] == b"2.1":
        if data[3:].decode() in os.listdir("./"):
            file_name = data[3:].decode()
            download(c,file_name)
        else:
            c.send("#wrong file name! try again!".encode())

        

    elif data[0:2] == b'3 ':
       upload(data,c)

    # elif data[0:2] == "4 ":
    #     file = open(filename_save,"wb")
    #     while True:
    #         data_recv = c.recv(4096)
    #         data_save = data_recv.decode()[3:].encode()
    #         file.write(data_save)
    #         if len(data_recv) < 4096/8:
    #             break
    #     file.close()


def child_process(c):
    #print("处理子进程的请求:",c.getpeername())
    try:
        while True:
            data = c.recv(4096)
            print(data)
            if not data:
                break
            data_handle(data,c)
    except (KeyboardInterrupt,SystemError):
        sys.exit("server stop")
    except Exception as e:
        print(e)
    c.close()
    sys.exit()
    

def ftp_server(host="",port=8888):
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind((host,port))
    s.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    #print("进程%d等待客户端连接"%os.getpid())

    while True:
        try:
            c, addr = s.accept()
            print("connected:", addr)
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            print(e)
            continue

        pid = os.fork()

        if pid == 0:
            s.close()
            child_process(c)
        else:
            c.close()
            continue

ftp_server()