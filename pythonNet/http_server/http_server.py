# http_server.py
from socketserver import *

# 创建服务器类
# class Server(ForkingMixIn,TCPServer):
# class Server(ForkingTCPServer):


class Server(ThreadingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):
    def handle(self):
        # self.request ==> accept 返回的套接字
        print("Connect from",
              self.request.getpeername())
        data = self.request.recv(8)
        print(data[0:3])
        if data[0:3] == b"GET":
            print("OK")
            self.return_web(data)
        else:
            pass

    def return_web(self, data1):
        while True:
            data = self.request.recv(1024)
            data1 += data
            print(data1)
            if len(data) < 1024:
                break
        request1 = data1
        # print(request)
        # 将request请求按行分割
        request_lines = request1.splitlines()
        line = request_lines[0].split(" ") [1]

        if line = '/' or line[-5:] = '.html':
            try:
                f = open("index.html")
            except IOError:
                response = "HTTP/1.1 404  not found\r\n"
                response += "\r\n"  # 空行
                response += "====Sorry not found====="
            else:
                response = "HTTP/1.1 200  OK\r\n"
                response += "\r\n"  # 空行
                response += f.read()
            finally:
                # 发送给浏览器
                print(response)
                self.request.send(response.encode())


if __name__ == "__main__":
    server_addr = ('127.0.0.1', 9998)
    #server_addr = ('127.0.0.1', 9998)
    # 创建服务器对象
    server = Server(server_addr, Handler)
    # 启动服务器
    server.serve_forever()
