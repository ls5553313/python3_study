# ftp_client.py

import os,sys
from socket import *
import signal
import time

def down_load(s):
    a = show_names(s)
    file_names = a[2:-2].split("\', \'")
    print(len(file_names))
    for x in range(len(file_names)):
        print(x,"-",file_names[x])
    while True:
        x = int(input("pls select a file: "))
        if x in range(len(file_names)):
            print("OK number")
            break
        else:
            print("wrong number!")
    s.send((b"2.1" + file_names[x].encode()))
    file_name = file_names[x] + '_download'
    

    file = open(file_name,"wb")
    while True:
        data_recv = s.recv(4096)
        #data_save = data_recv.decode()[3:].encode()
        file.write(data_recv)
        if len(data_recv) < 4096:
            break
    file.close()

def show_names(s):
    s.send(b"1")
    file_names = ""
    while True:
        data = s.recv(4096).decode()
        file_names += data
        print(file_names)
        if len(data) < 4096/8:
            break
    return file_names

def data_handle(option,s):
    if option == "1":
        print(show_names(s))
    elif option == "2":
        #print(show_names(s))
        down_load(s)


    elif option == "3":
        for x in range(len(os.listdir("./"))):
            print(x," - ",os.listdir("./")[x])
        while True:
            x = int(input("pls select a file: "))
            if x in range(len(os.listdir("./"))):
                print("OK number")
                break
            else:
                print("wrong number!")
        s.send(b"3 " + os.listdir("./")[x].encode())
        time.sleep(0.1)
        file = open(os.listdir("./")[x],"rb")
        while True:
            file_data = file.read(4096)
            #data_send = "2 ".encode() + file_data
            s.send(file_data)
            if len(file_data) < 4096:
                break
        file.close()
    elif option == "4":
        os._exit(0)
    else:
        print("wrong number")




    

def ftp_client():
    s = socket()
    s.connect(('127.0.0.1', 8888))
    while True:
        print('''pls select: 
    1. get file names
    2. download file
    3. upload file
    4. exit''')
        option = input()
        data_handle(option,s)




ftp_client()
