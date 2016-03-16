# -*- coding: utf-8 -*-

import requests
import serial

s = serial.Serial("/dev/ttyS0", 57600)

device_id = "DZF34Y80"          # 改成您的device id
device_key = "B0df4jYfaxQ0BwK9" # 改成您的device key
data_channel = "gamepad"        # 改成您遊戲手把的data channel id
data_channel2 = "gripper"       # 改成您開關控制的data channel id


url = "http://api.mediatek.com/mcs/v2/devices/" + device_id
url += "/datachannels/" + data_channel + "/datapoints.csv"

url2 = "http://api.mediatek.com/mcs/v2/devices/" + device_id
url2 += "/datachannels/" + data_channel2 + "/datapoints.csv"

def game_pad():  # 接受MCS gamepad資料通道的訊號 
    r = requests.get(url, headers = {"deviceKey" : device_key})
    data = r.content.split(',')[2:]
    return (data[0][0], data[0][-1])

def gripper():   # 接收MCS gripper資料通道的訊號
    r = requests.get(url2, headers = {"deviceKey" : device_key})
    return r.content[-1]

while True:      # 判斷接收到的訊號，並發送相對應的指令給Arduino端
    command = game_pad()
    command2 = gripper()
    if command[1] == "1":
        if command[0] == "l":
            print "press left"
            s.write("l")
        elif command[0] == "r":
            print "press right"
            s.write("r")
        elif command[0] == "u":
            print "press up"
            s.write("u")
        elif command[0] == "d":
            print "press down"
            s.write("d")
        elif command[0] == "A":
            print "press A"
            s.write("a")
        elif command[0] == "B":
            print "press B"
            s.write("b")
    if command2 == "1":
        print "closed"
        s.write("f")
    elif command2 == "0":
        print "open"
        s.write("o")
