import time

class MapWatchData():

    def __init__(self,imei,xloc,yloc,bat,rssi,sos,watch_date,create_date,is_position,address=''):
        self.imei = imei
        self.xloc = xloc
        self.yloc = yloc
        self.bat = bat
        self.rssi = rssi
        self.sos = sos
        self.watch_date = watch_date
        self.create_date = create_date
        self.is_position = is_position
        self.address = address