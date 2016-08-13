#
# Simple script to talk to the WMATA API and
# find out the number of elevators out of service
# on the Green Line today.
#
from __future__ import print_function
import json
try:
    from urllib2 import urlopen, Request
except ImportError:
    from urllib.request import urlopen, Request

demo_api_key = '6b700f7ea9db408e9745c207da7ca827'
url = 'https://api.wmata.com/Incidents.svc/json/ElevatorIncidents'
hdrs = {'api_key': demo_api_key}
req = Request(url, headers=hdrs)
response = urlopen(req)
raw_data = response.read()
string_data = raw_data.decode('utf8')
data = json.loads(string_data)
incidents = data['ElevatorIncidents']

stations_url = 'https://api.wmata.com/Rail.svc/json/jStations?LineCode=GR'
req2 = Request(stations_url, headers=hdrs)
response2 = urlopen(req2)
stations_data = json.loads(response2.read().decode('utf8'))
station_codes = []
stations_list = stations_data['Stations']
for s in stations_list:
    station_code = s['Code']
    station_codes.append(station_code)

for i in incidents:
    station_code = i['StationCode']
    if station_code in station_codes and i['UnitType'] == 'ELEVATOR':
        description = i['LocationDescription']
        location = i['StationName']
        print(location, description)
