import socket
import os
import hashlib

server = socket.socket()
server.bind(('localhost',9898))
server.listen(10)

conn,addr = server.accept()

while True:
    print('wait new instr...')
    data = conn.recv(1024)
    if not data:
        print('client closed..')
        break

    cmd,filename = data.decode().split()
    print(filename)
    print(os.path.isfile(filename))
    if os.path.isfile(filename):
        f = open(filename,'rb')
        # md5加密
        m = hashlib.md5()
        file_size = os.stat(filename).st_size
        print(file_size)
        conn.send(str(file_size).encode())
        # 等待客户端确认，防止粘包
        conn.recv(1024)

        # 遍历文件每一行
        for line in f:
            m.update(line)
            conn.send(line)
            pass
        # 16进制加密
        print('file md5:',m.hexdigest())
        f.close()
        conn.send(m.hexdigest().encode())
    print('send done')

server.close()