#
# Little script to check the WMATA API and find out
# how many elevators are out of service on the Green Line
# / when is the last train at a given stop
#
from __future__ import print_function
import json
try:
    from urllib2 import urlopen, Request
except ImportError:
    from urllib.request import urlopen, Request

api_key = '6b700f7ea9db408e9745c207da7ca827'
timings_url = 'https://api.wmata.com/Rail.svc/json/jStationTimes'  # [?StationCode]'

hdrs = {'api_key': api_key}
req = Request(timings_url, headers=hdrs)
result = urlopen(req)  # timeout=0.001
content = result.read().decode('utf8')  # 'cp1252'
data = json.loads(content)

station_times = data['StationTimes']
for time_info in station_times:
    code = time_info['Code']
    name = time_info['StationName']
    today_info = time_info['Saturday']
    last_trains = today_info['LastTrains']
    print(code, name)
    for train_info in last_trains:
        print("\t", train_info['Time'], train_info['DestinationStation'])
