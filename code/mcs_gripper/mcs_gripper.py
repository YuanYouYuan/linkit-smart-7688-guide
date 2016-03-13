import requests
import serial

s = serial.Serial("/dev/ttyS0", 57600)

device_id = "DZF34Y80"          # 改成您的device id
device_key = "B0df4jYfaxQ0BwK9" # 改成您的device key
data_channel = "gripper"        # 改成您的data channel id

url = "http://api.mediatek.com/mcs/v2/devices/" + device_id
url += "/datachannels/" + data_channel + "/datapoints.csv"

while True:
    r = requests.get(url, headers = {"deviceKey" : device_key}) # 讀取MCS上夾爪控制開關的訊號
    print r.content
    data = r.content.split(",")[2]
    if data == "1":             # 如果從MCS收到1，代表要開夾爪
        s.write("o")
    else if data == "0":        # 如果從MCS收到0，代表要閉夾爪
        s.write("f")
