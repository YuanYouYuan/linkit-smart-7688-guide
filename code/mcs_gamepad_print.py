# -*- coding: utf-8 -*-

import requests

device_id = "DZF34Y80"          # 改成您的device id
device_key = "B0df4jYfaxQ0BwK9" # 改成您的device key
data_channel = "gamepad"        # 改成您的data channel id

url = "http://api.mediatek.com/mcs/v2/devices/" + device_id
url += "/datachannels/" + data_channel + "/datapoints.csv"

print url 

while True:
    r = requests.get(url, headers = {"deviceKey" : device_key})
    print r.content
    data = r.content.split(",")[2]
    pressed = data.split("|")[1]
    key = data.split("|")[0]
    print "pressed: ", pressed, "\tkey: ", key, "\n"  # 印出是否被壓下按鈕及按鈕名稱
