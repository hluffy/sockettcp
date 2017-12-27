import socket

client = socket.socket()
client.connect(('localhost',9999))

while True:
    cmd = input('>>: ').strip()
    if len(cmd) == 0:
        continue

    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024)
    print('length: ', cmd_res_size)
    client.send('你瞅啥？'.encode('utf-8'))

    received_size = 0
    received_data = ''
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data.decode())
        # print(data)
        received_data += data.decode()
    else:
        print('cmd has received done....',received_size)
        print(received_data)

client.close()