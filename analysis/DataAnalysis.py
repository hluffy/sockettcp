# 262600db1230dd4637ee903732303135303932342c3130313933302c412c
# 32322e3536343032352c4e2c3131332e3234323332392c452c352e32312c
# 3135322c3130304031303133332c353137332c3436302c30312c36362d31
# 303133332c353137332c3436302c30312c36364033383a38333a34353a62
# 663a61663a61302c33342d65633a32363a63613a64393a30633a34612c34
# 382d36303a64383a31393a64323a39333a36342c35382d38303a38393a31
# 373a33623a38633a35652c35382d38383a32353a39333a31313a39383a38
# 662c36304031303040314031c6
from Until import trans

str = "262600db1230dd4637ee903732303135303932342c3130313933302c412c32322e3536343032352c4e2c3131332e3234323332392c452c" \
      "352e32312c3135322c3130304031303133332c353137332c3436302c30312c36362d31303133332c353137332c3436302c30312c3636403" \
      "3383a38333a34353a62663a61663a61302c33342d65633a32363a63613a64393a30633a34612c34382d36303a64383a31393a64323a3933" \
      "3a36342c35382d38303a38393a31373a33623a38633a35652c35382d38383a32353a39333a31313a39383a38662c36304031303040314031c6"
data = []
# type = ""
datastr = ''
for index in range(1,len(str)+1):
    datastr += str[index-1]
    if(index%2==0):
        if(index>4 and datastr=="26"):
            data.append("24")
            data.append("00")
            datastr = ""
            continue
        data.append(datastr)
        datastr = ""


my_data = data[12:]
gps_data = my_data[:my_data.index("40")]
gps = trans(gps_data)
print(gps.split(","))

my_data = my_data[my_data.index("40")+1:]
station_data = my_data[:my_data.index("40")]
station = trans(station_data)
print(station.split(","))

my_data = my_data[my_data.index("40")+1:]
wifi_data = my_data[:my_data.index("40")]
wifi = trans(wifi_data)
print(wifi.split(","))

my_data = my_data[my_data.index("40")+1:]
power_data = my_data[:my_data.index("40")]
power = trans(power_data)
print(power)

my_data = my_data[my_data.index("40")+1:]
g_sensor_data = my_data[:my_data.index("40")]
g_sensor = trans(g_sensor_data)
print(g_sensor)

my_data = my_data[my_data.index("40")+1:]
acc_data = my_data[:-1]
acc = trans(acc_data)
print(acc)


