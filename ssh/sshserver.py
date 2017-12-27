import socket
import os

server = socket.socket()
server.bind(('localhost',9999))
server.listen(5)

conn, addr = server.accept()

while True:


    data =conn.recv(1024)
    cmd_res = os.popen(data.decode()).read()
    print(len(cmd_res))
    if len(cmd_res) == 0:
        cmd_res = 'cmd has no output....'

    conn.send(str(len(cmd_res.encode())).encode('utf-8'))
    conn.send(cmd_res.encode('utf-8'))
    print('send done')

server.close()