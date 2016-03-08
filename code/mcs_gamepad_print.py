import requests

device_id = "DZF34Y80"
device_key = "B0df4jYfaxQ0BwK9"
data_channel = "gamepad"
url = "http://api.mediatek.com/mcs/v2/devices/" + device_id
url += "/datachannels/" + data_channel + "/datapoints.csv"

while True:
    r = requests.get(url, headers = {"deviceKey" : device_key})
    print r.content
    data = r.content.split(",")[2]
    pressed = data.split("|")[1]
    key = data.split("|")[0]
    print "pressed: ", pressed, "\tkey: ", key, "\n"
