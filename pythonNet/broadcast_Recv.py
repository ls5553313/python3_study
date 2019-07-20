from socket import *

sockdr = socket(AF_INET,SOCK_DGRAM)

sockdr.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

sockdr.bind(('0.0.0.0',9999))

while True:
    try:
        msg,addr = sockdr.recvfrom(1024)
        print("{},{}".format(addr,msg.decode()))
    except (KeyboardInterrupt, SyntaxError):
        raise
    except Exception as e:
        raise e

sockdr.close()