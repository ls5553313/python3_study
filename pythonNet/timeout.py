from socket import *
from time import sleep,ctime

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

s.settimeout(1)

while  True:
    print("waiting for connected...")
    try:
        c,addr =s.accept()
    except timeout:
        print(ctime())
        continue
    else:
        print("connect from", addr)
        while True:
            data = c.recv(1024).decode()
            if not data:
                break
            print(data)
            c.send(ctime().encode)
        c.close()
s.close()
