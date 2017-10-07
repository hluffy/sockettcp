import pymysql

from entity import MapWatchData

db = pymysql.connect()

cursor = db.cursor()

sql = "insert into map_watch_data_act(imei,xloc,yloc,bat,rssi,sos,watch_date,create_date,is_position,address)" \
      " values(1,2,3,100,0,0,'2017-12-12 00:00:00','2017-12-12 00:00:00','A','test')"

try:
    cursor.execute(sql)
    db.commit()
    print("save successed")
except:
    db.rollback()

db.close()

