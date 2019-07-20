#select_server.py

from select import select
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)



rlist = [s]
wlist = []
xlist = [s]

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("connected from", addr)
            c.send("WTF?".encode())
            rlist.append(c) 
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print(data.decode())
                wlist.append(r)
    for w in ws:
        w.send("Got your message!".encode())
        wlist.remove(w)
    for x in xs:
        if x is s:
            s.close()
    




