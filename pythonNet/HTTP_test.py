from socket import *

s = socket()

s.bind(('0.0.0.0',8000))

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.listen(5)

while True:
    c,addr = s.accept()
    print("connect from",addr)

    data = c.recv(4096)
    
    print("**********************")
    print(data.decode())
    print("**********************")

    data = '''HTTP/1.1 200 OK
    Conten-Encoding= gzip
    Content-Type= text/html

    <h1>WWWWW</h1>
    '''
    c.send(data.encode())
    c.close()
s.close()