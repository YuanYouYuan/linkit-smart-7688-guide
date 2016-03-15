# -*- coding: utf-8 -*-

import requests

device_id = "DZF34Y80"          # 改成您的device id
device_key = "B0df4jYfaxQ0BwK9" # 改成您的device key
data_channel = "gamepad"        # 改成您的data channel id

url = "http://api.mediatek.com/mcs/v2/devices/" + device_id
url = "/datachannels/" + data_channel + "/datapoints.csv"

def game_pad():
    r = requests.get(url, headers = {"deviceKey" : device_key})
    data = r.content.split(',')[2:]
    print data
    return (data[0][0], data[0][-1])

while True:
    command = game_pad()
    print command
    if command[1] == "1":
        if command[0] == "l":
            print "press left"
        elif command[0] == "r":
            print "press right"
        elif command[0] == "u":
            print "press up"
        elif command[0] == "d":
            print "press down"
        elif command[0] == "A":
            print "press A"
        elif command[0] == "B"
            print "press B"
