import socket

server = socket.socket()
server.bind(('localhost',6969))
server.listen(5)

print('服务端等待连接...')
while True:
    conn,addr = server.accept()
    print('有新的连接...')
    print(conn,addr)

    while True:
        data = conn.recv(1024)
        print('recv: ',data.decode())
        if not data:
            break
        conn.send(data.upper())

server.close()