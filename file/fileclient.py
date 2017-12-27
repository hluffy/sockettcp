import socket
import hashlib

client = socket.socket()
client.connect(('localhost',9898))

while True:
    cmd = input('>>: ').strip()
    if len(cmd)==0:
        continue

    if cmd.startswith('get'):
        client.send(cmd.encode())
        # 接收文件大小
        server_response = client.recv(1024)
        print('server response: ',server_response)
        # 向服务端发送确认信息，防止粘包
        client.send(b'ready to recv file')
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename+'new','wb')
        m = hashlib.md5()
        while received_size < file_total_size:
            # 判断已经发送的文件大小，设置size
            if file_total_size - received_size > 1024:
                size = 1024
            else:
                size = file_total_size - received_size
                print('last reveived: ',size)
            data = client.recv(size)
            received_size += len(data)
            m.update(data)
            f.write(data)
        else:
            new_file_md5 = m.hexdigest()
            print('file recv done ',received_size,file_total_size)
            f.close()

        server_file_md5 = client.recv(1024)
        print('server file md5: ',server_file_md5)
        print('client file md5: ',new_file_md5)