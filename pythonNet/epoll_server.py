# epoll_server.py
from socket import *
from select import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

p = epoll()
fdmap = {s.fileno(): s}
p.register(s, EPOLLIN | EPOLLERR)

while True:
    events = p.poll()
    for fd, e in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('connected from', addr)
            p.register(c, EPOLLIN | EPOLLHUP)
            fdmap[c.fileno()] = c
        elif e & EPOLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print(data.decode())
                fdmap[fd].send("Got your message!".encode())
