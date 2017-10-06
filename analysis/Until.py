def trans(data):
    str = ""
    for i in range(0,len(data)):
        str += chr(int(data[i],16))

    return str