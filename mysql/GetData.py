import pymysql


db = pymysql.connect("101.37.34.43","root","root","helemet")
print(db)

cursor = db.cursor()

sql = "select * from map_watch_data_act"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except:
    print("error")



db.close()