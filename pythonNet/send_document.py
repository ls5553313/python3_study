from socket import *

sockfd = socket()

sockfd.connect(('127.0.0.1', 8000))

while True:
    a = input("send>>")
    if not a:
        break
    file = open(a,"rb")
    
    while True:
        data = file.read(4096) #读入图片数据
        sockfd.send(data)
        if not data:
            #print('{0} send over...'.format(filepath))
            break
        print(data)
    file.close()
    #print(sockfd.recv(4096))

sockfd.close()