from socket import *

class TcpClient:
    HOST = '127.0.0.1'
    PORT = 12345
    BUFSIZE = 1024
    ADDR = (HOST, PORT)

    def __init__(self):
        self.client = socket(AF_INET,SOCK_STREAM)
        self.client.connect(self.ADDR)

        while True:
            data = input(">")
            if not data:
                break

            self.client.send(data.encode("utf-8"))
            print("发送数据到 %s: %s" %(self.HOST,data))

            if data.upper() == "QUIT":
                break

            data = self.client.recv(self.BUFSIZE)
            if not data:
                break

            print('从%s收到信息：%s' % (self.HOST, data.decode('utf8')))


if __name__ == '__main__':
    client = TcpClient()
