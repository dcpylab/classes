#
# Simple script to find out the number of
# elevators out of service on the Green Line
# today, using the WMATA API
#
import json
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

api_key = '6b700f7ea9db408e9745c207da7ca827'
incidents_url = 'https://api.wmata.com/Incidents.svc/json/ElevatorIncidents'

hdrs = {'api_key': api_key}
request = Request(incidents_url, headers=hdrs)
result = urlopen(request)
raw_data = result.read().decode('utf8')
data = json.loads(raw_data)
incidents = data['ElevatorIncidents']
elevator_incidents = []
for i in incidents:
    if i['UnitType'] == 'ELEVATOR':
        elevator_incidents.append(i)

# print(elevator_incidents[0])

station_list_url = 'https://api.wmata.com/Rail.svc/json/jStations?LineCode=GR'
request = Request(station_list_url, headers=hdrs)
result = urlopen(request)
raw_data = result.read().decode('utf8')
data = json.loads(raw_data)
stations = data['Stations']
station_codes = []
for s in stations:
    station_codes.append(s['Code'])

final_incidents = []
for i in elevator_incidents:
    if i['StationCode'] in station_codes:
        final_incidents.append(i)

print(final_incidents)
