# Http_Server.py

from socket import *

def handleClient(connfd):
    request = connfd.recv(4096)
    # print(request)
    request_lines = request.splitlines()
    for line in request_lines:
        print(line.decode())
    try:   
        f = open("index.html","r")
    except IOError:
        response = "HTTP/1.1 404 not found\r\n"
        response += "\r\n"
        response += "===sorry==="
    else:
        response = "HTTP/1.1 404 not found\r\n"
        response += "\r\n"
        response += f.read()
    finally:
        connfd.send(response.encode())


def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(("0.0.0.0",8888))
    sockfd.listen(3)
    print("listen to the port 8888")
    while True:
        connfd,addr = sockfd.accept()
        handleClient(connfd)
        connfd.close()

if __name__ == '__main__':
    main()