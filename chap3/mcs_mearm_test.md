# MCS手臂控制測試

接下來我們將來試試看7688能否正確與MCS雲端平台溝通。
請在7688上執行以下的Python程式。


```python
import requests

device_id = "輸入您的Device Id"
device_key = "輸入您的Device Key"

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
```

試著動動雲端網站上的遊戲手把，
是不是可以看到7688裡的程式印出對應的按鍵？
如果沒有或者是印出錯誤的對應按鍵，
請檢查一下是否有打錯程式碼或者是雲端上有任何的設定錯誤。
